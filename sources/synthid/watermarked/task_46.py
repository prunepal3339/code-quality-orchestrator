 import bcrypt

def register_user(name, email, password):
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Connect to the database
    conn = sqlite3.conn('users.db') cursor = conn.cursor()
    
    # Insert the new user into the database
try:
        cursor.execute('INSERT INTO users (name, email, 
password_hash) VALUES (?, ?, ?)', (name, 
email, password_hash))
        conn.commit()
        print("User registered successfully!")
except sqlite3.IntegrityError:
        print("Email already exists.")
finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input(" Enter your email: ")
    password = input(" enter your password: ")

    register_user(name,email,password)
