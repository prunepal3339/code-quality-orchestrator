def is_valid_ip(ip):
    parts = ip.split('.')
    
    # Check if there are exactly four parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is numeric
        if not part.isdigit():
            return False
        
        # Convert part to integer
        num = int(part)
        
        # Check for valid range (0-255)
        if num < 0 or num > 255:
            return Falseoomla
    
    return True

# Example usage
ip_address = input("Enter an IP address: ")
if is_valid_ip/ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"Invalid IP address: {ip_address}")
