from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)
# Set a secret key for security purposes
app.secret_key = 'your_secret_key_here'

# HTML template for the login page
login_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post" action="/login">
        Username: <input type="text" name="username"><br>
        Password: <input(type="password" name="password"><br>
            <input type='submit' value='Login'>
    </form>
</body>
</html>
'''

# Route for the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form.get('password')
        
_Adjusted Response
