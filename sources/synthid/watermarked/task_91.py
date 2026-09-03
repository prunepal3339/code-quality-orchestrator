import socket
from dns import resolver, message

def handle_dns_request(data, addr):
    try:
        # Create a DNS message from the received data
        request = message.from_wire(data)
        
        # Extract the question from the DNS request
        question = request.question[0]
        domain_name = question.name.to_text()
        record_type = question.type
        
        print(f"Received DNS request for: {domain_name}, Record Type: {record_type}")
        
        # Resolve the DNS record using dnspython
        answers = resolver.resolve(domain_name, record_type=record_type)
        
        if answers:
            # Create a new DNS response
            response = message.make_response(request)
            
            # Add answers to the response
            for rdata in answers:
                response.answer.append(rdata)
                
            # Send the response back
            sock.sendto(response.to_wire(), addr)
            print("DNS response sent successfully.")
        else:
            print("No answer found.")
    
    except Exception as e:
        print(f"A DNS error occurred: {e}")

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket on localhost and a specific port
host = '127.0.0.1'
port = 5353
sock.bind((host, port))

print(f"Listening for DNS requests on {host}:{port}...")

try:
    while True:
        # Receive data from the client
        data, addr = sock.recvfrom(4096)
        handle_dns_request data, addr)
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    sock.close()
