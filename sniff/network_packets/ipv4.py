import struct
from sniff.network_packets.utils import get_ipv4_address


class Ipv4:
    ICMP_PROTOCOL = 1
    TCP_PROTOCOL = 6
    UDP_PROTOCOL = 17

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.time_to_live, self.protocol, source, target = struct.unpack(
            '! 8x B B 2x 4s 4s', raw_data[:20])
        self.source = get_ipv4_address(source)
        self.target = get_ipv4_address(target)
        self.data = raw_data[self.header_length:]

    def get_info(self):
        print("Ip || source : {} ,target : {},protocol :{}".format(
            self.source, self.target, self.protocol))

    def get_other_ip(self, origin_ip):
        if self.target == origin_ip:
            return self.source
        else:
            return self.target
