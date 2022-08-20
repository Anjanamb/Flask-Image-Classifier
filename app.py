from flask import Flask, render_template, request

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2

app = Flask(__name__)
# model = VGG19


@app.route('/' ,methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/predict' ,methods = ['POST'])
def predict():
    if request.method == 'POST': 
        imagefile= request.files['imagefile']
        image_path= "./images/" + imagefile.filename
        imagefile.save(image_path)
        model = MobileNetV2(weights='imagenet')
        image = load_img(image_path, target_size=(224, 224))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        yhat = model.predict(image)
        label = decode_predictions(yhat)
        label = label[0][0]

        classification = '%s (%.2f%%)' % (label[1], label[2]*100)
        
        return render_template('index.html', prediction=classification)

if __name__ == '__main__':
    app.run(port = 3000,debug=True)