from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods placeholders=['POST'])
def submit():
    # Get data from form
    user_input = request.form['user_input']
    
替换为：

@app.route('/result')
def result():
    # Retrieve the user input from the session or directly from the URL parameter
    user_result = request.args.get('user_input', '')
    
    # Escape any potential HTML tags to prevent XSS
    safe_user_result = escape(user_result)
    
    return renderTemplate('result.html', user_result=safe_user_result)

if __name__ == '__main__':
    app.run(debug=True)
