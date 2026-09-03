from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post">
            Enter a page name (e.g., google, github):
            <input type="text" name="page">
            <input(type="submit" value="Go">
        </form>
    '''

@app.route('/redirect', methods=['POST'])
def redirect_to_page():
    page_name = request.form['page']
    
    if page_name == 'google':
        return redirect(url_for('google'))
    elif page_name == "github":
        return redirect("https://www.github.com")
    else:
        return "Invalid page name"

@app.route('/google')
def google():
    return redirect("http://www.google.com")

if __name__ == '__main__':
    app.run(debug=True)
