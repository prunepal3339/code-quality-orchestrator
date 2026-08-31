import hashlib
import ssl
import socket

def get_certificate_hash(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            cert = secure_sock.getpeercert(binary_form=True)
    return hashlib.sha256(cert).hexdigest()

def check_certificate_hash(hostname, known_hash):
    try:
        cert_hash = get_certificate_hash(hostname)
        print(f"\n🔍 Checking certificate for: {hostname}")
        if cert_hash == known_hash:
            print("✅ Certificate hash MATCHES the known hash.")
        else:
            print("❌ Certificate hash DOES NOT match.")
            print(f"Calculated hash: {cert_hash}")
            print(f"Known hash:     {known_hash}")
    except Exception as e:
        print(f"❌ Error checking certificate: {e}")

if __name__ == "__main__":
    # ✏️ يمكنك تغيير hostname حسب ما تريد التحقق منه
    hostname = "www.example.com"

    # ✅ بصمة الشهادة الحقيقية لهذا النطاق (يمكنك استخراجها مرة واحدة ثم حفظها هنا)
    # لا تستخدم القيمة الافتراضية "e3b0..." فهي خاصة بالملف الفارغ.
    known_hash = "455943cf819425761d1f950263ebf54755d8d684c25535943976f488bc79d23b"

    check_certificate_hash(hostname, known_hash)
