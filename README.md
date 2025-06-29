# Camera Object Detection System with YOLOv5

This repository contains all code, scripts, configuration files, and model artifacts developed as part of our object detection project using YOLOv5. The system is designed to detect people, weapons (primarily pistols), and specific body parts (hands, heads, legs), including combinations like "person holding a gun".

---

## Repository Structure

The project includes:
- Python source code
- Training scripts
- Pre-trained and fine-tuned model weights
- Supporting tools (camera calibration, distortion correction, labeling utilities)
- YOLOv5-based inference and training utilities  
> **Note:** The dataset used for training is **not** included here and must be downloaded separately (see below).

---

## Dataset

The datasets were collected from [Roboflow Universe](https://universe.roboflow.com), focusing on YOLOv5-compatible formats (images + YOLO `.txt` annotations).

We manually curated and combined several datasets that include:
- People
- Pistols
- Hands, heads, legs
- Person-with-gun combinations

**Final dataset:**
- Over 100,000 labeled images
- Used for both training and validation

---

##Environment Setup

1. **Install Python 3.8**  
   > Other versions may cause incompatibility issues.

2. **Clone the YOLOv5 repo (or use our included version)**

3. **Install dependencies** using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Dataset YAML Configuration

The dataset paths are defined in the file:  
`pistol_person_dataset.yaml`

Example:
```yaml
train: C:/Users/eeproj/Desktop/Project/train_person_with_part_pistol_new
val: C:/Users/eeproj/Desktop/Project/valid_person_with_part_pistol_new
```

---

## Training

To train the model on your dataset:
```bash
python train.py --img 640 --batch 16 --epochs 5 --data pistol_person_dataset.yaml --weights yolov5l.pt
```

Model outputs are saved automatically to:
```
runs/train/exp75/
```
The main result file is `best.pt` – the final trained weights.

---

## Real-Time Detection

To perform real-time detection with your webcam:
```bash
python detect.py --weights runs/train/exp75/weights/best.pt --img 640 --conf 0.4 --source 1
```

- Use `--source 0` for the default laptop webcam  
- Use a video file path for offline detection (e.g., `--source video.mp4`)

---

## Project Scripts

| File Name                         | Description |
|----------------------------------|-------------|
| `object_detection.py` (was `detect.py`) | Main YOLOv5 detection script with distortion correction |
| `image_undistortion.py` (was `undistort.py`) | Removes camera distortion based on calibration |
| `camera_calibration.py` (was `test2.py`) | Calibrates camera using chessboard pattern |
| `live_camera_view.py` (was `test4.py`) | Shows live feed post-correction (no detection) |
| `gui_launcher.py` (was `tes1.py`) | Graphical interface for launching the system |
| `label_fix_single_object.py` (was `person_files_repair_test.py`) | Fixes label files (e.g. changes "person" class to 1) |
| `label_validation_multi_object.py` (was `test.py`) | Validates labels vs. images in dataset |

---

## Usage Instructions

1. Set up Python 3.8
2. Install dependencies
3. Prepare YOLOv5 and your dataset
4. Train using `train.py`
5. Run detection using `detect.py` or `object_detection.py`
6. Use additional tools for camera calibration and GUI control

