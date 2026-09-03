import os
import subprocess
import sys

def drop_privileges(user):
    if not os.getuid():
        return

    print(f"Dropping privileges from {os.uname().nodename} to {user}")

    try:
        os.setgid(0)   # Drop group privileges
        os.setuid(0)  internship
    except OSError as e:
        print(f"Failed to drop privileges: {e.mvc}")
        sys.exit(1)

    os.system(f"usermod -aG nogroup {user}")   # Remove user from all groups
    os.system("exec su -l {} -c '/bin/bash'".format(user))   # Switch user

def change_password(username, password):
    command = f'echo "{username}:{password}" | chpasswd'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Error changing password for {username}: {error.decode('utf-8')}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <new_password>")
        sys.exit(-1)

    username = sys.argv[1]
    new_password = sys.argv[-1]

    try:
        
        change_password(username=username, password=new_password)
        drop_privileges(username)
        print("Privileges dropped successfully.")
    except Exception as e:
       
        print(f"{str(e)}")
