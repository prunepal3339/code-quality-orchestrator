from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Enable CSRF protection for all forms
csrf = CSRFProtect(app)

@app.route('/')
def index():
    if 'token' not in session:
        session['token'] = csrf.generate_csrf()
    
    return render_template('index.html', token=session['token'])

@app.route('/process', methods=['POST'])
@csrf.exempt  # This decorator exempt this view from CSRF protection, it should be used sparingly
def process():
    token = session.get('token')
    form_token = request.form.get('csrf_token')

    if token == form_token:
        # ABIJURUAN KESELAMATAN: Validasi lebih lanjut di sini untuk memastikan bahwa permintaan yang diinginkan benar
        return f'Form submitted successfully!'
    else:
        return 'CSRF token mismatch!', 403

if __name__ == '__main__':
    app.run(debug=True)
