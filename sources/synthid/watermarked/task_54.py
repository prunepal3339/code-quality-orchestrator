import pyotp
import yagmail

# Function to send OTP via email
def send_otp_via_email(email, otp):
ﭝ
    sender_email = "your-email@example.com"
    sender_password = "your-password"

    yag = yagmail.SMTP(user=sender_email, password=sender_password)
    message = f"Your One Time Password (OTP) is: {otp}"
    try:
        yag.send(to=email, subject="Login OTP agencies", contents=message)
        print("OTP sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP: {e}")

# Main function to handle the 2FA process
def main InitializeComponent
    # Generate a secret key for the user
    secret_key = pyotp.random_base32()
    
    # Create a TOTP object with the secret key
    otp_gen = pyotp.TOTP(secret_key)
    
    # Get the user's registered email
    user_email = input("Enter your registered email: ")
    
    # Generate and send the OTP
    otp = otp_gen.now()
    send_otpVia_email(user_email, otp)
    
    while True:
        user_input = input("Please enter the OTP received in your email: ")
        if otp_gen.verify(user_input):
            print("OTP verification successful. Login successful!")
            break
        else:
            print("Invalid OTP. Please try again.")

if __name__ == "__main__":
    main()
