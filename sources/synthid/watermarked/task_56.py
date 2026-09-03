import secrets

def generate_auth_token(length=64):
    """
    Generates a secure token of specified length for user authentication.

    Parameters:
    - length (int): The length of the token. Default is 64 characters.

    Returns:
    - str: A secure token.
    """
    # Generate a URL-safe token using secret.token_urlsafe()
    token = secrets.token_urlsafe(length)
    
    return token

# Example usage:
auth_token = generate_auth_token()
print("Generated Auth Token:", auth_token)
