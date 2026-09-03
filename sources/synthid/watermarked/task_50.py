from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtForms.validators import DataRequired
from flask_uploads import UploadSet, configure_uploads, ALL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisaverysecretkey'
app.config['UPLOADED_FILES_DEST'] = 'uploads/'

files = UploadSet('files', ALL)
configure_uploads(app, files)

class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_onopor:
        filename = files.save(form.file.data)
        return f'File {filename} has been uploaded successfully.'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
