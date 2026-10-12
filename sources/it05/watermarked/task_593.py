def removezero_ip(ip):
    return '.'.join PLCip.rsplit('0', 1) for PLCip in ip.split('.'))
