# AI Coding Agent Instructions for UAO-Neumonía Detector

## Project Overview
**Purpose:** Medical diagnostic support tool for pneumonia detection and classification from chest X-ray images using deep learning with explainability (Grad-CAM visualization).

**Classification Categories:** Bacterial Pneumonia, Viral Pneumonia, Normal (no pneumonia)

**Tech Stack:** TensorFlow/Keras CNN model, Tkinter GUI, OpenCV image processing, DICOM/JPG support, Python 3.8+

---

## Critical Architecture & Data Flow

### Single-File Monolithic Structure
All functionality exists in [detector_neumonia.py](../detector_neumonia.py) with modular functions:
- **Image Input:** `read_dicom_file()` / `read_jpg_file()` - loads and converts image formats to RGB arrays
- **Preprocessing:** `preprocess()` - resizes to 512x512, converts to grayscale, applies CLAHE histogram equalization, normalizes to [0,1], reshapes to batch tensor (1,1,512,512,1)
- **Model Inference:** `predict()` - chains preprocessing → model loading → prediction → Grad-CAM heatmap generation
- **Explainability:** `grad_cam()` - targets layer "conv10_thisone" (last conv layer), computes class activation gradients, generates jet colormap overlay at 0.8 transparency

### Neural Network Architecture
CNN based on Pasa et al. (Efficient Deep Network Architectures for Chest X-Ray TB Screening):
- **5 convolutional blocks** with skip connections (16→32→48→64→80 filters, 3×3 kernels)
- **Max pooling** after each block, **average pooling** after block 5
- **3 fully-connected layers:** 1024, 1024, 3 neurons (output: bacterial/normal/viral)
- **Regularization:** 20% dropout on blocks 4, 5 and after 1st dense layer
- **Pre-trained model:** Binary file `WilhemNet86.h5` (not in repo, loaded by `model_fun()` - implementation missing)

### GUI Application Class (`App`)
Tkinter-based interface with:
- **State management:** Stores image array, prediction results, report counter
- **Image display areas:** Two 250×250 text widgets showing original and heatmap images
- **Critical workflow:** Load image → Enable "Predecir" button → Run model → Display label, probability, heatmap
- **Export features:** Save to CSV (`historial.csv`), generate JPG screenshots → PDF

---

## Essential Conventions & Patterns

### Image Handling
- **Medical DICOM format:** Uses `pydicom.read_file()` → extracts `pixel_array` → normalizes to 0-255 uint8 range
- **Grayscale processing:** All images converted to grayscale for model input (single channel)
- **Standard preprocessing:** Resize → Grayscale → CLAHE (Contrast Limited Adaptive Histogram Equalization) → Normalize → Batch reshape
- **Output visualization:** Heatmap overlays use OpenCV's JET colormap (high intensity on predicted region) blended at 80% transparency

### TensorFlow/Keras Specifics
- **Eager execution disabled:** Line 18 uses TF1.x compatibility mode: `tf.compat.v1.disable_eager_execution()` + `output_all_intermediates(True)`
- **Model access:** Uses `model.get_layer("conv10_thisone")` by string name - layer naming is critical
- **Gradient computation:** Uses `K.gradients()` (backend) for manual Grad-CAM implementation
- **Batch format required:** Model expects (1, 512, 512, 1) tensor shape

### Prediction Output Format
Returns tuple: `(label_string, probability_percent, heatmap_array_BGR)`
- Labels: "bacteriana" (idx 0), "normal" (idx 1), "viral" (idx 2)
- Probability: Float 0-100 representing confidence percentage

---

## Development Workflow & Environment Setup

### Environment Configuration
```bash
# Create TensorFlow conda environment (from README)
conda create -n tf tensorflow
conda activate tf
pip install -r requirements.txt
python detector_neumonia.py
```

### Key Dependencies (from [requirements.txt](../requirements.txt))
- `tensorflow` - deep learning framework
- `opencv-python` - image processing (resize, colorspace conversion, colormap)
- `pydicom` - medical image format reading
- `pillow` - image display in Tkinter
- `img2pdf` - JPG to PDF conversion
- `pyautogui` - screenshot functionality
- `tkcap` - Tkinter window capture
- `pandas` - data handling (referenced in requirements, not visibly used)
- `python-xlib` - X11 support for GUI rendering

### Current Issues to Address
1. **Missing imports:** Lines 1-20 of detector_neumonia.py have incomplete imports - missing `import tensorflow as tf`, `import pydicom as dicom`, `import tensorflow.keras.backend as K`
2. **Missing model function:** `model_fun()` called but not defined - must load `WilhemNet86.h5`
3. **Deprecated PIL methods:** `Image.ANTIALIAS` removed in Pillow 10.0.0 - use `Image.LANCZOS` instead
4. **TF1 compatibility mode:** Disable eager execution works for inference but requires careful gradient computation syntax
5. **Docker incompleteness:** Dockerfile references nonexistent main.py - should call detector_neumonia.py

---

## Integration Points & Cross-Component Communication

### GUI ↔ Model Pipeline
```
load_img_file() → stores array → run_model() 
  → predict(array) → preprocess() → model inference → grad_cam()
  → display results in text widgets
```

### File I/O
- **CSV logging:** Appends patient ID, predicted label, confidence to `historial.csv` (delimiter: "-")
- **Image capture:** `tkcap.CAP()` captures Tkinter window → JPG → PIL conversion → PDF save
- **Model loading:** Must be from file path (hardcoded or configurable)

### Gradient Computation Dependencies
- Grad-CAM requires direct access to model layers and activations
- Target layer "conv10_thisone" must exist and be named exactly
- Uses `K.function()` for eager evaluation of intermediate activations

---

## Testing & Validation Patterns
- **Sample DICOM files:** Available at Google Drive link in README (used for manual testing)
- **Expected accuracy:** Model trained on tuberculosis screening dataset, applied to pneumonia - cross-domain transfer
- **Validation method:** Visual inspection of Grad-CAM heatmaps (should highlight lung regions) + prediction labels
- **GUI testing:** Manual interaction - load image, verify button state transitions, check CSV output

---

## When Extending This Project

### Adding Features
- **New image formats:** Add new functions `read_<format>_file()` following [read_dicom_file](../detector_neumonia.py#L68) pattern
- **Model updates:** Replace `WilhemNet86.h5` and update layer name in `grad_cam()` [line 25](../detector_neumonia.py#L25)
- **Additional exports:** Add export methods to `App` class using `tkcap` capture paradigm
- **GUI improvements:** Follow Tkinter ttk widget convention; use StringVar for reactive state management

### Critical Gotchas
1. **Image dimensions:** Model strictly requires 512×512 input - any other size breaks inference
2. **Colorspace:** Must be grayscale (1 channel) after preprocessing
3. **Batch dimension:** Always (1, H, W, 1) shape - missing batch dim causes "incompatible shape" errors
4. **TensorFlow versions:** TF1/TF2 compatibility modes are fragile - test eager vs. graph modes
5. **DICOM medical data:** Pixel values can have arbitrary ranges - must normalize before display and inference
