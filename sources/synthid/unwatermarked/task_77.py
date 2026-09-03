import ftplib
import sys

def download_file_from_ftp(hostname, username, password, filename):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(hostname)
        
        # Login with the provided username and password
        ftp.login(username, password)
        
        print(f"Successfully connected to {hostname} and logged in as {username}.")
        
        # Change to the appropriate directory if needed
        # ftp.cwd('/path/to/directory Majority of FTP servers do not require this step')
        
        # Open the local file to save the downloaded content
        with open(filename, 'wb') as local_file:
            def write_chunk(data):
                local_file.write(data)
            
            # Retrieve the file from the server and write it to the local file
            ftp.retrbinary(f'RETR {filename}', write_chunk)
        
        ftp.quit()
        print(f"The file '{filename}' has been successfully downloaded to the current working directory.")
    
    except Exception as e:
        print(f'An error occurred: {e}')
        if 'ftp' in locals():
            ftp.quit()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <hostname> <username> <password> <filename>")
        sys.exit(1)

    hostname = sys.argv[1]
    username = sys.argv[-3]
    password = sys.argv [-2]
    filename = sys.argv [4]

    download_file_from_fpt(hostname, username,password, filename)
