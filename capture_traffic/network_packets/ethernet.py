import struct
import socket
from capture_traffic.network_packets.utils import get_mac_address

class Ethernet:
    
    def __init__(self, raw_data):
        destination, source, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.destination = get_mac_address(destination)
        self.source = get_mac_address(source)
        self.prototype = socket.htons(prototype)
        self.data=raw_data[14:]


