Device telemetry publisher

Use this from the actual Raspberry Pi / Colibry application.

The publisher intentionally does not create FPS, detection, CPU, RAM or model values. Your real inference/application loop supplies those values.

Example payload:

from telemetry_client import publish

publish({
    "project": "gesture-recognition",
    "online": True,
    "fps": real_fps,
    "latency_ms": real_latency_ms,
    "cpu_percent": real_cpu_percent,
    "ram_percent": real_ram_percent,
    "current_detection": real_gesture,
    "confidence": real_confidence,
    "camera": "CONNECTED",
    "model": "LOADED",
    "accelerator": "AIDGE CPU",
    "extra": {"hands": real_hands, "uart_status": real_uart_status},
})

For EdgeGuard, use project: edgeguard and provide real detection/model/NPU values.

Set on the device:
PORTFOLIO_API_URL=https://your-api-domain.example
DEVICE_TOKEN=<secret device token>

Never commit the real device token to GitHub.
