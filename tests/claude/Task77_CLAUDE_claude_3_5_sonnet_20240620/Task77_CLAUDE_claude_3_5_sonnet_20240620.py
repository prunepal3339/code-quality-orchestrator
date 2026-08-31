
import sys
from ftplib import FTP

def download_file(hostname, username, password, filename):
    try:
        with FTP(hostname) as ftp:
            ftp.login(username, password)
            with open(filename, 'wb') as local_file:
                ftp.retrbinary(f'RETR {filename}', local_file.write)
        print(f"File {filename} downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <hostname> <username> <password> <filename>")
        sys.exit(1)
    
    hostname, username, password, filename = sys.argv[1:]
    download_file(hostname, username, password, filename)

# Run the code:
# ┌──(kali㉿kali) - [~]
# └─$ cd / home / kali / PycharmProjects / llm - generated - code - python / tests
#
# ┌──(kali㉿kali) - [~ / PycharmProjects / llm - generated - code - python / tests]
# └─$ cd
# claude / Task77_CLAUDE_claude_3_5_sonnet_20240620
#
#
# ┌──(kali㉿kali) - [~ /… / llm - generated - code - python / tests / claude / Task77_CLAUDE_claude_3_5_sonnet_20240620]
# └─$ python3
# Task77_CLAUDE_claude_3_5_sonnet_20240620.py
# ftp.gnu.org
# anonymous
# anonymous @ README