from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
# Set a secret key to keep the client-side sessions secure
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Check if the user is already logged in
    if 'username' in session:
        return 'Logged in as %s' % session['username']
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        # Here you would normally check if the username and password match your database records
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input tpye="password" name="password"><br>
           <input type = "submit" value = "Login">
        </form inse
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url For('index'))

if __name__ == '__main__':
    app.run(debug=True)
