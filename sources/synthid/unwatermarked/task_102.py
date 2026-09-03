import hashlib
import sqlite3

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to update user password in the database
def update_user_password(username, new_password):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Hash the new password
    hashed_password = hash_password(new_password)
    
    # Update the user's password in the users table
    try:
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        print(f"Password updated successfully for {username}.")
    except sqlite3.Error as e:
        print(f"A database error occurred: {e}")
    finally:
        # Close the connection
        conn.close()

# Example usage
if __name__ == "__main__":
    username = input("Enter your username: ")
    new_password = input(" Enter your new password: ")
    
    update_user_password(filename, new_password)
