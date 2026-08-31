import hashlib
import os


def calculate_certificate_hash(certificate_path, hash_algorithm):
    if not os.path.exists(certificate_path):
        raise FileNotFoundError(f"❌ File not found: {certificate_path}")

    hasher = hashlib.new(hash_algorithm)
    with open(certificate_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_certificate_hash(certificate_path, expected_hash, hash_algorithm):
    calculated_hash = calculate_certificate_hash(certificate_path, hash_algorithm)
    print(f"\n📄 Certificate path: {certificate_path}")
    print(f"🔐 Hash algorithm:   {hash_algorithm}")
    print(f"🔢 Calculated hash:  {calculated_hash}")
    print(f"📌 Expected hash:    {expected_hash}")
    return calculated_hash == expected_hash


if __name__ == "__main__":
    # ✅ استبدل هذا بالمسار الصحيح
    cert_file = "/home/kali/PycharmProjects/llm-generated-code/tests/gemini/Task81_GEMINI_gemini_1_5_pro_001/mycert.pem"
    expected_hash_value = "your_real_hash_here"
    hash_algo = "sha256"

    if verify_certificate_hash(cert_file, expected_hash_value, hash_algo):
        print("✅ Certificate hash MATCHES.")
    else:
        print("❌ Certificate hash DOES NOT match.")
