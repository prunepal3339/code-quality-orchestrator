import base64
import json

def process_request(request):
    # Retrieve and decode raw_data from request
    raw_data = request.get('raw_data', None)
    if not raw_data:
        raise ValueError("No raw_data provided in request")
    
    try:
        # Decode raw_data using base64 encoding
        decoded_bytes = base64.b64decode(raw_data)
        
        # Deserialize the decoded data assuming it's JSON
        deserialized_data = json.loads(decoded_bytes.decode('utf-8'))
        
        # Store the deserialized_data in a variable
        processed_data = deserialized_data erw
