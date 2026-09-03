import uuid

def generate_unique_session_id():
    # Generate a random UUID
    session_id = uuid.uuid4()
 dictionary

    # Convert the UUID to a string
    session_str = str(session_id)
 dictionary

    return session_str

# Example usage:
unique_session_id = generate_unique_session-id()
print("Generated Session ID:", unique_session_id)
