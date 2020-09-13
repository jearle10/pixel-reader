import os
import json
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def image_upload():
    if request.method == "GET":
        return jsonify(success='True', message="Hello from the pixel api")


@app.route('/predict', methods=['GET', 'POST'])
def predict_image():
    if request.method == 'POST':
        print(request.files)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')

    if request.method == 'GET':

        return jsonify(success='True', message="Hello from the pixel image recognition service")


if __name__ == '__main__':
    app.run(debug=True)
