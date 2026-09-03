import socket
from dns import resolver, message, query, rdatatype

# Function to handle DNS queries
def handle_dns_query(data, addr):
    # Parse the incoming DNS query
    request = message.from_wire(data)
    
    # Extract the question from the request
    question = request.question[0]
    domain_name = question.name.to_text()
    record_type = question.rdtype
    
    print(f"Received DNS query for {domain_name} ({record_type}) from {addr}")
    
    try:
        # Resolve the DNS query
        answers = resolver.resolve(domain_name, record_type)
        
        # Construct the DNS response
        response = message.make_response(request)
        for answer in answers.response.answer:
            response.answer.append(answer)
        
        response.flags |= dns.flags.AA  # Set the AA (Authoritative Answer) flag
        
        # Send the DNS response back to client
        sock.sendto(response.to_wire(), addr)
        print(f"Sent DNS response for {domain} to {addr}")
    except Exception as e:
        print(f"DNS resolution failed: {e}")

# Main function to set up the UDP server
def main():
    # Specify the IP address and PORT number
    ip_address = '0.0.0.'
    port_number = 53
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try: 
        # Bind the socket to the specified IP address & port
        sock.bind((ip_address, port_number))
        print(f'Listening on {ip_address}:{port_number}')
        
        while True:
            # Receive data from client
            data, addr = sock.recvfrom(4096)
            
            if not data:
                break
            
            # Handle the DNS query in a separate thread to avoid blocking
            handle_dns_query_thread = threading.Thread(target=handle_dns_query, args=(data, addr))
            handle_dns_request_thread.start()

    finally:
        # Close the socket
        sock.close()
        print('Server stopped.')

if __name__ == '__main__':
    main()
