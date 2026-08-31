import socket
from dnslib import DNSRecord, DNSHeader, QTYPE, RR, A

def resolve_dns(data):
    try:
        request = DNSRecord.parse(data)
        qname = request.q.qname
        qtype = QTYPE[request.q.qtype]

        print(f"🔎 Received DNS query for {qname} (type: {qtype})")

        # Create DNS response with dummy IP
        response = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)

        # Example: respond with 192.168.1.1 for any A record
        if request.q.qtype == QTYPE.A:
            answer = RR(
                rname=qname,
                rtype=QTYPE.A,
                rdata=A("192.168.1.1"),
                ttl=60
            )
            response.add_answer(answer)

        return response.pack()

    except Exception as e:
        print(f"❌ Failed to resolve: {e}")
        return None

def main():
    server_ip = "0.0.0.0"
    server_port = 5353  # use 5353 instead of 53 to avoid needing sudo

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))

    print(f"✅ DNS server is running on {server_ip}:{server_port}")

    while True:
        data, addr = sock.recvfrom(512)
        response = resolve_dns(data)
        if response:
            sock.sendto(response, addr)
            print(f"✅ Response sent to {addr[0]}:{addr[1]}\n")

if __name__ == "__main__":
    main()
