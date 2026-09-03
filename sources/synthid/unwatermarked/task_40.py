from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtform.validators import DataRequired
from wtflask.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key
csrf = CSRFProtect(app)

class SettingsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Update')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SettingsForm()
    if form.validate_on_submit():
        username = form.username.data
        # Here you would typically save the username to the database
        flash(f'Username updated to {username}', 'success')
        return redirect(url_for('index'))
    return render_template('settings.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
