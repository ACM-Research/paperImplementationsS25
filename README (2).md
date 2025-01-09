# YOLO Scene Graph Generator

A Python project that generates scene graphs from images using YOLO object detection and spatial relationship analysis.

## Overview

This project combines YOLO object detection with a custom neural network to:
1. Detect objects in images using YOLOv8
2. Analyze spatial relationships between detected objects
3. Generate a scene graph representing object relationships
4. Visualize the resulting scene graph

## Requirements

- Python 3.x
- PyTorch
- Ultralytics YOLO
- NetworkX
- PyTorch Geometric
- Matplotlib
- NumPy

## Installation

```bash
pip install ultralytics torch torch_geometric networkx matplotlib numpy