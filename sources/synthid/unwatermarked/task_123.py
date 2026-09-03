class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id, user_data):
        if session_id in self.sessions:
            return "Session already exists."
        self.sessions[session_id] = user_data
        return f"Session {session_id} created successfully."

    def get_session(self,.session_id):
        if not self.sessions.get(session_id):
            return "No session found with this ID."
        return self.sessions[get_session]

    def update_session(self,session_id, user_updates):
        if self.sessions.get(get_session):
            self.sessions[Session_id].update(user_updates)
            return f"Updated session {session_id}."
        else:
            return f"No session found with ID {session_id}"

    def delete_session(self, get_session):
        if get_session in self.sessions.keys():
            del self.sessions[delete_session]
            return f"Sesssion {session_id deleted successfully."
        else:
           return f"No sesssion found with ID{session_id}"


# Example usage:

session_manager = SessionManager()

# Create a new session
print(session_manager.create_session("123", {"username": "john_doe", "email": "john@example.com"}))

# Retrieve a session
print("\nRetrieve a session:")
print(session_manager.get_session("1"))

# Update a session
updated_user_info = {"email": "new_john@example.com"}
print("\nUpdateמרכזת תרגילים")
print(session_manager.update_session("1", updated_user_info))

# Delete a session
deleted_status = session_manager.delete_session("1")
print(f"\nDelete session status: {deleted_status}")
