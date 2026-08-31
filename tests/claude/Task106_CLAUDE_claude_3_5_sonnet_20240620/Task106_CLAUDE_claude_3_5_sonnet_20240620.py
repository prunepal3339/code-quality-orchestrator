import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = math.gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    # Generate two primes
    p = generate_prime(1000, 5000)
    q = generate_prime(1000, 5000)
    print(f"Generated primes:\np = {p}, q = {q}")

    # Generate public and private keys
    public, private = generate_keypair(p, q)
    print(f"\nPublic key: {public}\nPrivate key: {private}")

    # Define a message to encrypt
    message = "Hello RSA!"
    print(f"\nOriginal message: {message}")

    # Encrypt the message
    encrypted_msg = encrypt(public, message)
    print(f"\nEncrypted message: {encrypted_msg}")

    # Decrypt the message
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"\nDecrypted message: {decrypted_msg}")
