from sqlalchemy import createammable
from werkzeug.security import generate_password_hash

# Establishing a connection to the database (Replace 'mydatabase', 'username', and 'password' with your actual credentials)
engine = create_engine('postgresql://username:password@localhost/mydatabase')

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

def update_user_password(username, new_password):
    # Querying the User table for a record with the given username.
    user = session.query(User).filter_by(username=username).first()

    if user:
        # Hashing the new password.
        hashed_password = generate_password_hash(new_password)

        # Updating the password in the database.
        user.password = hashed_password
        session.commit()
        print("Password updated successfully.")
    else:
        print("User not found.")

# Replace 'example_username' and ' Kushner' with your desired username and new_password
update_user_password('example_username', 'Kushner')
