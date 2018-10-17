import struct
from capture_traffic.network_packets.utils import get_ipv4_address


class Ipv4:

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.time_to_live, self.prototocol, src, target = struct.unpack(
            '! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = get_ipv4_address(src)
        self.target = get_ipv4_address(target)
        self.data = raw_data[self.header_length:]
