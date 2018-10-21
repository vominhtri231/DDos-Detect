from dos_analyze.dos_para import Dos_para


class Analyze_result():
    def __init__(self):
        self.map = dict()

    def set_icmp(self):
        self.map[Dos_para.IS_ICMP] = 1

    def set_syn(self):
        self.map[Dos_para.IS_SYN] = 1

    def set_ack(self):
        self.map[Dos_para.IS_ACK] = 1

    def set_dns_in(self):
        self.map[Dos_para.IS_DNS_IN] = 1

    def set_dns_out(self):
        self.map[Dos_para.IS_DNS_OUT] = 1

    def merge(self, other):
        for key in other.map:
            frequency = other.map[key]
            if key in self.map:
                self.map[key] += frequency
            else:
                self.map[key] = frequency
