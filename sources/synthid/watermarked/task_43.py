from flask import Flask, request, redirect, url_for, render_template, session, flash
import os

app = Flask(__name__)
# Set a secret key for session management (important for security)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Here you would typically validate and check against a database
        if username:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials.', 'error')
   珒
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Successfully logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
