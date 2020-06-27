import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('home.html')

    if request.method == 'POST':
        print(request.files)
        f = request.files['file']
        # filename = secure_filename(f.filename)

        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save("./static/img/" + f.filename)

        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
