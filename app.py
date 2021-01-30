from __future__ import division, print_function
# coding=utf-8
import os
import numpy as np

# Keras
from keras.preprocessing import image
from keras.models import load_model

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

model = load_model('models/Inception-ResNet-v2-2.h5')
print('ResNetV2 Model loaded.')
print('Running on http://localhost:5000')

def get_file_path_and_save(request):
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    return file_path


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predictResNetV2', methods=['GET', 'POST'])
def predictResNetV2():
    if request.method == 'POST':
        file_path = get_file_path_and_save(request)

        # Read label names
        label_names = list()

        with open('labels_desription.txt', 'r') as f:
            for line in f:
                label_names.append(line.split('. ')[1].strip())

        img = image.load_img(file_path, target_size=(224, 224))

        # Preprocessing the image
        x = image.img_to_array(img)
        x = np.true_divide(x, 255)
        x = np.expand_dims(x, axis=0)

        # Make prediction
        pred = model.predict(x)[0]

        answer = []

        for ind, label_ind in enumerate(np.argsort(pred)[::-1][:3]):
            answer.append('{0}. {1} with {2}% probability.'. \
                  format(ind+1, np.sort(label_names)[label_ind].capitalize(),
                         np.round(pred[label_ind]*100, 1)))

        answer.append('Document name: ' + file_path.split('\\')[-1] + '.')

        return '; '.join(answer)
    return None


if __name__ == '__main__':
    # Serve the app with gevent
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
