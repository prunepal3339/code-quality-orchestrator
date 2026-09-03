import subprocess
import os

def change_user_password(username, new_password):
    try:
        # Change the user's password using the 'passwd' command
        subprocess.run(['sudo', 'chage', '-d', '0', username], check=True)
        subprocess.run(f'echo "{username}:{new_password}" | sudo chpasswd', shell=True, check=True)
        
        print(f"Password changed successfully for user {username}.")
        
        # Drop root privileges
        if os.getuid() == 0:
            os.setuid(1000)  # Assuming the regular user ID is 1001, adjust accordingly
        
        print("Dropped root privileges.")
    
    except subprocess.CalledProcessError as e:
        print(f"A problem occurred while changing the password: {e}")
    except PermissionError as e2:
        print("Permission denied. You need to run this script with elevated privileges (root).")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print('Please run this script as root or with sudo.')
        exit()

    username = input("Enter the username whose password you want to change: ")
    new_password = input("New password: ")

    change_user_password(user, new_password)
