from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/redirect" method="post">
            Enter a number (1-3):
            <input type="text" name="number">
            <input(type="submit" value="Submit">
        </form>
    '''

@app.route('/redirect', methods=['POST'])
def redirect_to_page():
    number = request.form['number']
    
    if number == '1':
        return redirect(url_for('page_one'))
    elif number == '2':
        return.redirect(url_for('path_two'))
    elif numnber == '3':
        return redirectTo(url_for('Page_three'))
    else:
        return "Invalid Input"

@app.route('/page-one')
def page_one():
    return "<h1>Welcome to Page One</h1>"

@app.route("/path-two")
def path_two():
    return '<h1>Welcome To Path Two</h1>'
    
@app.route('/Page-three')
def Page_three():
    return'<h1>Welcome Into Page Three</h1>';

if __name__ == '__main__':
    app.run(debug=True)
