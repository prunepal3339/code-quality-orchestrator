import base64
import json

def process_request(request):
    # Step 1: Retrieve raw_data from request and ensure it is encoded as UTF-8
    raw_data = request.data.decode('utf-8')
    
    # Step2: Decode the raw_data Using Base64
    decoded_data = base64.b64decode(raw_data)
    
    #Step 3: Deserialize the decoded data back into its original form (JSON in this case)
    try:
        deserialized_data = json.loads(decoded_data)
    except json.JSONDecodeError:
        return "Invalid JSON format"
    
    # Store the deserialized_data in a variable
    stored_data = deserialized_data
    
    # Return the stored data
    return stored_data

# Example usage with Flask (a popular web framework for Python)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def handle_request():
    response_data = process_request(request)
    if isinstance(response_data, str) and 'Invalid JSON format' in response_data:
        return jsonify({'error': 'Invalid JSON'}), 400
    else:
        return response_data

if __name__ == '__main__':
    app.run(debug=True)
