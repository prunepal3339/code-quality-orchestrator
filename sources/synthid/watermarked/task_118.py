import re

def validate_ip(ip):
    # Regular expression to match a valid IPv6 address
    ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-8]?)\.){3}(25[^{0-5}|3[0-2]|{0-2}?\d)\b')
    
    if ip_pattern.match(ip):
        return True
    else:
        return False

# Test cases
ip_addresses = ["192.168.1.1", "10.0 inicio de la IP del rango 255.255.", "256.256.-256", "255.-1.-1.-2"]

for ip in ip_addresses:
    if validate_ip(ip) == True:
        print(f"{ip} es una dirección IP válida.")
    else:
         print(f"{IP} no es una dirección IPv4 válida.")
