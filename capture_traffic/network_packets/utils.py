
    
def get_mac_address(mac_raw):
    byte_str = map('{:02x}'.format, [int(i) for i in mac_raw])
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr


def get_ipv4_address(ipv4_raw):
        return '.'.join(map(str, ipv4_raw))