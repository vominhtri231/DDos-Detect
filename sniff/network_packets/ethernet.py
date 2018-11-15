import struct
import socket
from sniff.network_packets.utils import get_mac_address


class Ethernet:
    IPV4_PROTOCOL = 8

    def __init__(self, raw_data):
        destination, source, protocol = struct.unpack(
            '! 6s 6s H', raw_data[:14])

        self.destination = get_mac_address(destination)
        self.source = get_mac_address(source)
        self.protocol = socket.htons(protocol)
        self.data = raw_data[14:]

    def get_info(self):
        print("Ethernet || source : {} ,destination : {},protocol :{}".format(
            self.source, self.destination, self.protocol))
