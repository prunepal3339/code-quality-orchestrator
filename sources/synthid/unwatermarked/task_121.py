from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
 comprises of two functions: one for rendering the HTML form and another for handling the file upload.

def index():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def uploader_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'no selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File successfully uploaded'

if __name__ == '__main__':
    app.run(debug=True)
