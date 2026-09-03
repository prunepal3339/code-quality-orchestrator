from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
# Set a secret key to keep the client-side sessions secure.
app.secret_key = 'your_secret_key'

# Route to handle login requests.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume we have a username and password verification function here.
        verify_user(request.form['username'], request.form['password']):
            # If user is authenticated, store their username in the session.
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input tpye="password" name="password"><br>
           <input type = submit value=Login>
        </form>
    '''

# Route to display user's home page.
@app.route('/')
def home():
    if 'username' in session:
        return f"Logged in as {session['username']}<br><a href='/logout'>Logout</a>"
    return "You are not logged in<br><a href='login'>Login</a>"

# Route to log out the user.
@app.route("/logout")
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url For('home'))

# Check if run directly (not imported).
if __name__ == '__main__':
    app.run(debug=True)
