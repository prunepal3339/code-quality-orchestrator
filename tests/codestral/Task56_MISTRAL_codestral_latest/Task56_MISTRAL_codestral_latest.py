import hashlib
import time

def generate_token(username, password):
    timestamp = str(time.time())
    data = username + password + timestamp
    token = hashlib.sha256(data.encode()).hexdigest()
    return token

print (generate_token("user","password"))
# 4b941e3c6efb5910a25aaa6a5c11ac9598869212ea643c96efa0780bc55c5855