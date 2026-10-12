def removezero_ip(ip):
    return '.'.join([str(int(octet)) for octet in ip.split('.')])
