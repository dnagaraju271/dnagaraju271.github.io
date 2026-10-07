# Portfolio Live Backend

Python/FastAPI backend for the public read-only live dashboards.

Architecture:

Visitor -> Portfolio frontend -> HTTPS API -> latest telemetry
                                      ^
                                      |
                              protected device POST
                                      ^
                                      |
                            Raspberry Pi / Colibry

Public status endpoints expose telemetry only. Device ingestion requires X-Device-Token. Owner inspection requires X-Owner-Token.

Local run:
1. cd backend
2. python3 -m venv .venv
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. cp .env.example .env
6. uvicorn app.main:app --reload --port 8001

Health endpoint: /health
Public status: /api/projects/gesture-recognition/status

Security boundary:
- Do not expose the Raspberry Pi directly to the public internet.
- Use HTTPS in production.
- The Raspberry Pi should make an outbound authenticated connection to the API.
- Public visitors receive read-only telemetry.
- Owner/admin endpoints require separate authentication.
- No endpoint executes shell commands, GPIO operations, model uploads, or arbitrary code.

The in-memory telemetry store is a development scaffold. A production deployment should use a managed store or database for historical telemetry.
