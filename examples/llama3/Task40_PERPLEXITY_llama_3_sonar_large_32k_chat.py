# Python (using Flask framework)
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'secret_key_here'

@app.route('/update_settings', methods=['GET', 'POST'])
def update_settings():
    if request.method == 'POST':
        if 'csrf_token' not in session or session['csrf_token'] != request.form['csrf_token']:
            return 'CSRF token is invalid'
        # Update user settings here
        return 'Settings updated successfully'
    csrf_token = session['csrf_token'] = 'random_token_here'
    return f'''
        <form action="" method="post">
            <input type="hidden" name="csrf_token" value="{csrf_token}">
            <label>Username:</label>
            <input type="text" name="username"><br><br>
            <label>Email:</label>
            <input type="email" name="email"><br><br>
            <input type="submit" value="Update Settings">
        </form>
    '''

if __name__ == '__main__':
    app.run()