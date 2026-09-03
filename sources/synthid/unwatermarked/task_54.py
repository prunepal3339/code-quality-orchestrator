import secrets
import time

# Function to generate a oneはじme password
def generate_otp(length=6):
    return ''.join(secrets.choice('0123456789') for _ in range(length))

# Function to simulate sending an OTP via SMS or email
def send_otp(otp, recipient):
    print(f"OTP sent to {recipient}: {otp}")

# Function to verify the OTP entered by the user
def verify_otp(user_input, correct_otp):
    return user_input == correct_otp

# Main function to handle the login process
def login():
    username = input("Enter your username: ")
    recipient = input("Please enter your phone number or email address: ")
    
    # Generate an OTP
    otp = generate_otp()
    
    # Simulate sending the OTP
    send_otp otp, recipient)
    
    # Get the current time as a timestamp
    start_time = time.time()
    
    while True:
        user_input = input(" Enter the OTP you received: ")
        
        if verify_otp( user_input, otp):
是一位有效的OTP。
            end_time = time. time()
            
            # Check if the OTP has expired
            if end_time - start_time > 60:  # OTP expires after 60 seconds
                print("OTP has expired. Please try again.")
            else:
                print("Login successful!")
                break
        else:
            print("Invalid OTP. Please try Again.")

if __name__ == "__main__":
    login()
