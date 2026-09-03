import uuid

def generate_session_id():
    # Generate a random UUID and convert it to a string
    return str(uuid.uuid4())

# Example usage
session_id = generate_session_id()
print("Generated Session ID:", session_id)
