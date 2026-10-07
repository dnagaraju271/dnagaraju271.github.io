import os
from datetime import datetime, timezone
from typing import Any
from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
APP_ENV = os.getenv("APP_ENV", "development")
PORTFOLIO_ORIGIN = os.getenv("PORTFOLIO_ORIGIN", "http://127.0.0.1:8000")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN", "")
OWNER_TOKEN = os.getenv("OWNER_TOKEN", "")

app = FastAPI(title="Nagaraju Dharavath — Embedded AI API", version="0.1.0")
allowed_origins = [PORTFOLIO_ORIGIN]
if APP_ENV == "development":
    allowed_origins += ["http://localhost:8000", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(dict.fromkeys(allowed_origins)),
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-Device-Token", "X-Owner-Token"],
)

class DeviceTelemetry(BaseModel):
    project: str = Field(pattern=r"^[a-z0-9-]+$")
    online: bool
    timestamp: datetime
    fps: float | None = None
    latency_ms: float | None = None
    cpu_percent: float | None = None
    ram_percent: float | None = None
    detections: int | None = None
    current_detection: str | None = None
    confidence: float | None = None
    camera: str | None = None
    model: str | None = None
    accelerator: str | None = None
    extra: dict[str, Any] = {}


MESSAGES = {
    "en": "Device offline or no telemetry received yet.",
    "fr": "Appareil hors ligne ou aucune télémétrie reçue pour le moment.",
    "de": "Gerät offline oder noch keine Telemetriedaten empfangen.",
    "es": "Dispositivo sin conexión o aún no se han recibido datos de telemetría.",
    "hi": "डिवाइस ऑफलाइन है या अभी तक कोई telemetry प्राप्त नहीं हुई है।",
    "te": "డివైస్ ఆఫ్‌లైన్‌లో ఉంది లేదా ఇంకా telemetry అందలేదు.",
    "ta": "சாதனம் ஆஃப்லைனில் உள்ளது அல்லது இதுவரை telemetry பெறப்படவில்லை.",
    "ja": "デバイスがオフライン、またはまだテレメトリを受信していません。",
    "zh": "设备离线或尚未收到遥测数据。"
}

def request_language(accept_language: str | None) -> str:
    code = (accept_language or "en").lower().split(",")[0].split("-")[0]
    return code if code in MESSAGES else "en"

latest: dict[str, DeviceTelemetry] = {}

def require_device_token(x_device_token: str | None = Header(default=None)) -> None:
    if not DEVICE_TOKEN or x_device_token != DEVICE_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid device credentials.")

def require_owner_token(x_owner_token: str | None = Header(default=None)) -> None:
    if not OWNER_TOKEN or x_owner_token != OWNER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Owner authentication required.")

@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": "portfolio-api", "environment": APP_ENV, "time": datetime.now(timezone.utc).isoformat()}

@app.get("/api/projects/{project}/status")
def project_status(project: str, accept_language: str | None = Header(default=None)) -> dict[str, Any]:
    item = latest.get(project)
    if item is None:
        return {"project": project, "online": False, "message": MESSAGES[request_language(accept_language)]}
    return item.model_dump(mode="json")

@app.get("/api/projects")
def projects() -> dict[str, Any]:
    return {"projects": [
        {"id": "gesture-recognition", "live": True, "read_only": True},
        {"id": "edgeguard", "live": True, "read_only": True},
    ]}

@app.post("/api/device/telemetry", dependencies=[Depends(require_device_token)])
def ingest_telemetry(payload: DeviceTelemetry) -> dict[str, Any]:
    latest[payload.project] = payload
    return {"accepted": True, "project": payload.project}

@app.get("/api/admin/telemetry", dependencies=[Depends(require_owner_token)])
def admin_telemetry() -> dict[str, Any]:
    return {"projects": {key: value.model_dump(mode="json") for key, value in latest.items()}}
