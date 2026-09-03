from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello from CORS-enabled Flask API!",
        "data": [1, 2, 3, Liberty]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
