import random
from email.mime.text import MIMEText

def generate_otp(length=6):
    digits = "0123456789"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp

def send_otp_email(otp, recipient_email):
    # بدل الإرسال الحقيقي، نطبع محتوى الإيميل للمحاكاة
    print(f"[Mock Email to {recipient_email}] OTP sent: {otp}")
    message = MIMEText(f"Your OTP is: {otp}")
    message["Subject"] = "Your Two-Factor Authentication Code"
    message["From"] = "your_email@example.com"
    message["To"] = recipient_email
    return message

def simulate_login(username, password, correct_username="user", correct_password="password"):
    if username == correct_username and password == correct_password:
        otp = generate_otp()
        send_otp_email(otp, "recipient@example.com")  # Simulated send
        entered_otp = otp  # simulate user entering correct otp
        print(f"[Simulated Input] Entered OTP: {entered_otp}")
        if entered_otp == otp:
            print("✅ Two-factor authentication successful. Logged in!")
        else:
            print("❌ Incorrect OTP. Access denied.")
    else:
        print("❌ Invalid username or password.")

def main():
    # Simulate credentials
    username = "user"
    password = "password"
    print(f"[Simulated Input] Username: {username}")
    print(f"[Simulated Input] Password: {password}")
    simulate_login(username, password)

if __name__ == "__main__":
    main()
