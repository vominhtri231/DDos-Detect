import struct


class Udp:

    def __init__(self, raw_data):
        self.source_port, self.destination_port= struct.unpack('! H H', raw_data[:4])
        self.data = raw_data[8:]
