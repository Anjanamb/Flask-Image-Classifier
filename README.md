# Flask Image Classifier

> Flask web app for real-time image classification using a pretrained **MobileNetV2** (ImageNet weights). Upload an image, get the top class with confidence.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## Features

- Upload any image via a Bootstrap-styled web form
- Real-time classification using MobileNetV2 pretrained on ImageNet (1000 classes)
- Predicted label + confidence percentage

## Project structure

```
Flask-Image-Classifier/
├── app.py                # Flask application
├── templates/
│   └── index.html        # Bootstrap upload form
└── images/               # Uploaded images (auto-saved)
```

## Quickstart

```bash
git clone https://github.com/Anjanamb/Flask-Image-Classifier.git
cd Flask-Image-Classifier
pip install flask tensorflow
python app.py
```

Open `http://127.0.0.1:3000/`, upload an image, click **Predict Image**.

## How it works

The uploaded image is resized to 224×224, preprocessed for MobileNetV2, and decoded with `decode_predictions`. Example output:

```
Labrador retriever (95.23%)
```

## Roadmap

- [ ] Top-K predictions (not just top-1)
- [ ] Display the uploaded image alongside the prediction
- [ ] Dockerfile
- [ ] Fine-tuning script for custom datasets

## License

[MIT](LICENSE) — see [anjanamb.github.io](https://anjanamb.github.io/) for more projects.
