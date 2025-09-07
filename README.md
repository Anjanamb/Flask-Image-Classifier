# Flask-Image-Classifier

>A simple **Flask web app** for real-time **image classification** using a pretrained **MobileNetV2** deep learning model (ImageNet weights).  

>Users can upload an image through the web interface, and the app predicts the most likely class with confidence.

---

## Features

- Upload any image via the web interface
- Real-time classification using **MobileNetV2**
- Displays predicted label with confidence percentage
- Web UI styled with **Bootstrap**
- Easy to run locally

---

## Project Structure
```
Flask-Image-Classifier/
├── app.py # Flask application
├── templates/
│ └── index.html # Frontend (Bootstrap upload form)
└── images/ # Uploaded images (auto-saved here)
```

---

## Requirements

- Python **3.8+**
- Install dependencies:
  ```bash
  pip install flask tensorflow

---

## Usage

### 1. Clone the repo
```bash
git clone https://github.com/Anjanamb/Flask-Image-Classifier.git
cd Flask-Image-Classifier
```

### 2. Run the Flask app
```bash
python app.py
```

### 3. Open in browser
```bash
http://127.0.0.1:3000/
```

### 4. Upload an image
- Select an image file.
- Click Predict Image.
- The prediction and confidence will be displayed.

---

## Model Details
- Uses MobileNetV2 pretrained on ImageNet (1000 classes).
- Image is resized to 224x224, preprocessed, and fed to the model.
- Output is decoded using decode_predictions.

Example prediction output:
```java
Labrador retriever (95.23%)
```
---

## Future Improvements
- Support for multiple top predictions
- Display uploaded image alongside prediction
- Add Docker support for easier deployment
- Deploy on cloud (Heroku, AWS, etc.)
- Option to fine-tune MobileNetV2 with custom dataset

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
