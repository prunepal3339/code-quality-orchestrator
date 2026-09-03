from flask import Flask, request, redirect, url_for, render_template_string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 16024  # Set maximum file size to 16MB
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new file</ illegal>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <br><br>
          <button type=submit value=upload>Upload</button>
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'File does not have a filename'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD-folder'], filename))
        return f'File {filename} has been uploaded successfully!'
    else:
        return f'Sorry, we do not support {file.filename.split(".")[-1]} file extension'

if __name__ == '__main__':
    app.run(debug=True)
