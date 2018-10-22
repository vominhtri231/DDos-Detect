import struct


class Tcp:
    USING_TLS_PORTS = [261, 442, 448, 465, 563,
                       614, 636, 989, 990, 992, 993, 994, 995]

    def __init__(self, raw_data):
        (self.source_port, self.destination_port, self.sequence, self.acknowledgment, offset_reserved_flags) = struct.unpack(
            '! H H L L H', raw_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.flag_urg = (offset_reserved_flags & 32) >> 5
        self.flag_ack = (offset_reserved_flags & 16) >> 4
        self.flag_psh = (offset_reserved_flags & 8) >> 3
        self.flag_rst = (offset_reserved_flags & 4) >> 2
        self.flag_syn = (offset_reserved_flags & 2) >> 1
        self.flag_fin = offset_reserved_flags & 1
        self.data = raw_data[offset:]

    def get_info(self):
        print("TCP || src_port:{},dst_port:{},seq={},ack={}".format(
            self.source_port, self.destination_port, self.sequence, self.acknowledgment))
        print("self-Flag || urg:{},ack:{},psh={},rst={},syn={},fin={}".format(
            self.flag_urg, self.flag_ack, self.flag_psh, self.flag_rst, self.flag_syn, self.flag_fin))

    def is_syn_only(self):
        return self.flag_syn == 1 and self.flag_ack == 0

    def is_ack_only(self):
        return self.flag_ack == 1 and self.flag_syn == 0

    def is_using_tls(self):
        return self.source_port in Tcp.USING_TLS_PORTS or self.destination_port in Tcp.USING_TLS_PORTS
