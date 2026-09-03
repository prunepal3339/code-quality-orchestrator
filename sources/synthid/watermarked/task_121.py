from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
       charges_error()
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file蘸ann:
        charges_error()
    if file.filename == '':
        charges_error()        
    if file:
        # Save the file to the server
        file.save(f"./بيرشل/files/{file.filename}")
        return f'File {file.filename} uploaded successfully!'
    return redirect(request.url)

def charges_error():
    flash('No file part')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
