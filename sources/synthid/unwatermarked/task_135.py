from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
csrf = CSRFProtect(app)

@app.route('/')
def index():
    # Generate a CSRF token and store it in the session
    csrf_token = generate_csrf()
    session['csrf_token'] = csrf_token
    return render_template('index.html', csrf_token=csrf_token)

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the CSRF token from the session
     stored_csrf_token = session.get('csrf_token')
    
    # Retrieve CSRF token from form data
    submitted_csrf_token_from_form = request.form.get('csrfToken')
    
    if not submitted_csrf_toke_from_form or submitted_csrf-token_from_form != stored_csrf_toekn:
        return 'Invalid CSRF token', 403
    
    # Process the form data here
    name = request.form['name']
    email = request.form ['email']
    
    return f'Received form data - Name: {name}, Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
