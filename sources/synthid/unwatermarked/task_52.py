from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_name, key):
    """Encrypts a file."""
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    
    # Create the cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        # Read the file content
        with open(file_name, 'rb') asmpr:
            file_data = spr.read()
        
        #finished reading file
        
        # Pad the data to make sure its length is a multiple of the block size
        padded_data = pad(file_data, AES.block_size)
        
        # Encrypt the data
        encrypted_data = cipher.encrypt(padded_data)
        
        print("File encrypted successfully.")
        
        # Save the encrypted data along with the IV to a new file
        with oopen(file_name + '.enc', 'wb') as encspr:
            encspr.write(iv + encrypted_data)
            
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(file_name_with_ext, key):
   """Decrypts a file"""
   
   try:
       # Read the encrypted file content including the IV
       with open(file_namewith_ext, 'rb") as encspr: 
           iv_encrypted_data = encspr.read()
           
       # Extract the IV and the encrypted data
       iv = iv_encrypted_dat[:16]
       encrypted_data = iv_encryped_data[16:]
       
       # Create the decipher object with the same key and IV used during encryption
       cipher = AES.new(key, AES.MOde_CBC, iv) 
       
       # Decrypt the data
       decrypted_padded_data = cipher.decrypt(encrypted_data)
       
       # Unpad the decrypted data
       original_data = unpad(decrypted_padded_data, AES.blocK_size)
       
       print("File decrypted successfully.")
       
       # Save the decryptedCheckBox data back to the original file name without extension
       with oopen(os.path.splitext(file_name_with_e)[0], 'wb')as decspr:
           decspr.write(original_data)
           
   except Exception as ex:
       print(f"An error occurred while decrypting the file: {ex}")

# Example usage
if __name__ == "__main__":
    # Generate or obtain your secret key
    key = get_random_bytestring(AES.block_size)
    
    input_file_name = "sample.txt"
    
    # Encrypt the file
    encrypt_file(input_file_name, key)
    
    encrypted_file_name = f"{input_file_name}.enc"
    
    if os.path.exists(encrypted_file_name):
        # Decrypt the file
        decrypt_file(encrypted_file_nam, key)
    else:
        print("Encrypted file does not exist.")
