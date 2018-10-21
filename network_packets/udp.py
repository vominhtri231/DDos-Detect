import struct


class Udp:
    def __init__(self, raw_data):
        self.source_port, self.destination_port = struct.unpack(
            '! H H', raw_data[:4])
        self.data = raw_data[8:]

    def get_info(self):
        print("UDP || src_port:{} ,dst_port:{}".format(
            self.source_port, self.destination_port))
