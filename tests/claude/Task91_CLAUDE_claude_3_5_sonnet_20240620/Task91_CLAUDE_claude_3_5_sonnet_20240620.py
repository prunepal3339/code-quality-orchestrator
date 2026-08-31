import socket
import struct
import dns.resolver
import dns.rdatatype


def parse_dns_query(data):
    # Extract query details from DNS packet
    id = struct.unpack('!H', data[:2])[0]
    qdcount = struct.unpack('!H', data[4:6])[0]

    domain = ''
    offset = 12
    while True:
        length = data[offset]
        if length == 0:
            offset += 1
            break
        domain += data[offset + 1:offset + 1 + length].decode() + '.'
        offset += length + 1
    domain = domain.rstrip('.')

    qtype = struct.unpack('!H', data[offset:offset + 2])[0]
    qclass = struct.unpack('!H', data[offset + 2:offset + 4])[0]

    return id, domain, qtype, qclass


def resolve_dns(domain, qtype):
    try:
        answers = dns.resolver.resolve(domain, dns.rdatatype.to_text(qtype))
        return [str(rdata) for rdata in answers]
    except Exception as e:
        print(f"Resolution error: {e}")
        return []


def create_dns_response(id, domain, qtype, qclass, answers):
    packet = struct.pack('!H', id)
    packet += struct.pack('!H', 0x8180)  # standard response, no error
    packet += struct.pack('!H', 1)  # QDCOUNT
    packet += struct.pack('!H', len(answers))  # ANCOUNT
    packet += struct.pack('!H', 0)  # NSCOUNT
    packet += struct.pack('!H', 0)  # ARCOUNT

    # Question section
    for part in domain.split('.'):
        packet += struct.pack('B', len(part))
        packet += part.encode()
    packet += b'\x00'
    packet += struct.pack('!H', qtype)
    packet += struct.pack('!H', qclass)

    # Answer section
    for answer in answers:
        packet += b'\xc0\x0c'  # pointer to domain
        packet += struct.pack('!H', qtype)
        packet += struct.pack('!H', qclass)
        packet += struct.pack('!I', 300)  # TTL
        packet += struct.pack('!H', 4)  # RDLENGTH (IPv4)
        packet += socket.inet_aton(answer)

    return packet


def main():
    server_ip = '127.0.0.1'
    server_port = 5353  # use high port to avoid permission issues

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))

    print(f"✅ DNS server running on {server_ip}:{server_port}")

    while True:
        data, addr = sock.recvfrom(512)
        id, domain, qtype, qclass = parse_dns_query(data)
        print(f"🔎 Query from {addr[0]}: {domain} (type {qtype})")

        answers = resolve_dns(domain, dns.rdatatype.to_text(qtype))
        response = create_dns_response(id, domain, qtype, qclass, answers)

        sock.sendto(response, addr)
        print(f"✅ Response sent to {addr[0]}:{addr[1]}\n")


if __name__ == "__main__":
    main()
