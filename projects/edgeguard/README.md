# EdgeGuard — Embedded AI on Colibry

## Overview

EdgeGuard is Nagaraju Dharavath's embedded AI project for deploying computer-vision inference on edge hardware. The **Colibry platform and NPU/SDK work are part of EdgeGuard**, not a separate project.

## Current direction

- Human and animal detection
- Real-time computer vision
- YOLO / ONNX model deployment
- AIDGE inference workflow
- Colibry NPU / embedded acceleration
- Linux and embedded development
- Future object tracking and performance benchmarking

## Architecture

Camera → preprocessing → YOLO/ONNX → AIDGE/NPU → detection → live dashboard

## Hardware

- Colibry evaluation hardware
- Camera input
- Embedded Linux development environment where applicable

## Software

- Python
- OpenCV
- YOLOv8
- ONNX
- AIDGE
- Linux

## Next milestones

1. Validate reliable human/animal detections.
2. Integrate the real Colibry NPU execution path.
3. Measure FPS, latency and resource usage.
4. Add object tracking.
5. Connect the live device to the portfolio dashboard securely.
