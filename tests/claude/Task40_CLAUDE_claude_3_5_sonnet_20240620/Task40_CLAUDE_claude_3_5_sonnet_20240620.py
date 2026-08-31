from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for CSRF
csrf = CSRFProtect(app)

class SettingsForm(FlaskForm):  # Corrected to use FlaskForm
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Update Settings')

@app.route('/', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        return 'Settings updated successfully!'
    return render_template('settings.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
