"""Authenticated telemetry publisher for Raspberry Pi / Colibry applications.

This module does not generate telemetry. The running edge application must provide
real values in the payload dictionary.
"""
import os
from datetime import datetime, timezone
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("PORTFOLIO_API_URL", "").rstrip("/")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN", "")

def publish(payload: dict[str, Any]) -> dict[str, Any]:
    if not API_URL:
        raise RuntimeError("PORTFOLIO_API_URL is not configured.")
    if not DEVICE_TOKEN:
        raise RuntimeError("DEVICE_TOKEN is not configured.")
    payload = dict(payload)
    payload.setdefault("timestamp", datetime.now(timezone.utc).isoformat())
    response = requests.post(
        f"{API_URL}/api/device/telemetry",
        json=payload,
        headers={"X-Device-Token": DEVICE_TOKEN},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()
