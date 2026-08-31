import hashlib
import ssl
import os


def get_cert_hash(cert_path):
    if not os.path.exists(cert_path):
        raise FileNotFoundError(f"❌ File not found: {cert_path}")

    with open(cert_path, "rb") as cert_file:
        cert_data = cert_file.read()

    # Convert DER to PEM (if the input is a binary .crt/.der file)
    pem_cert = ssl.DER_cert_to_PEM_cert(cert_data)

    # Compute SHA-256 hash of the PEM string (as UTF-8 bytes)
    cert_hash = hashlib.sha256(pem_cert.encode('utf-8')).hexdigest()
    return cert_hash


def main():
    # ✅ عدّل المسار والبصمة حسب شهادتك
    cert_path = "/home/kali/PycharmProjects/llm-generated-code/tests/gtp4o/Task81_OPENAI_gpt_4o/mycert.crt"
    known_hash = "your_known_hash_here"

    try:
        cert_hash = get_cert_hash(cert_path)
        print(f"\n📄 Certificate path: {cert_path}")
        print(f"🔢 Calculated hash: {cert_hash}")
        print(f"📌 Known hash:      {known_hash}")

        if cert_hash == known_hash:
            print("✅ Certificate matches the known hash.")
        else:
            print("❌ Certificate does NOT match the known hash.")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
