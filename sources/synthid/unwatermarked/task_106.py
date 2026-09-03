import rsa

# Generate public and private keys
(pubkey, privkey) = rsa.newkeys(512)

# Data to be encrypted
data = 'Hello World'

# Encrypting the data
encrypted_data = rsa.encrypt(data.encode(), pubkey)
print('Encrypted:', encrypted_data)

# Decrypting the data 
decrypted_data = rsa.decrypt(encrypted_data, privkey).decode()
print('Decrypted:', decrypted_data)
