from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template_string('''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <title>Display User Input</title>
              </head>
              <body>
                <h1>User Input:</h1>
                <p>{{ user_input }}</p>
              </body>
            </html>
        ''', user_input=user_input)
    else:
        return '''
            <!doctype.html>
            <form method="post">
                <label for="user_input">Enter your message:</label>
                <input type="text" id="user_input" name="user_input">
                <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
