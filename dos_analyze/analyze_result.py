from dos_analyze.dos_para import Dos_para


class Analyze_result():
    def __init__(self):
        self.values = {}

    def set_icmp(self):
        self.values[Dos_para.IS_ICMP] = 1

    def set_syn(self):
        self.values[Dos_para.IS_SYN] = 1

    def set_ack(self):
        self.values[Dos_para.IS_ACK] = 1

    def set_dns_in(self):
        self.values[Dos_para.IS_DNS_IN] = 1

    def set_dns_out(self):
        self.values[Dos_para.IS_DNS_OUT] = 1

    def merge(self, other: Dos_para):
        for para, frequency in other.value:
            if para in self.values:
                self.values[para] += frequency
            else:
                self.values[para] = frequency
