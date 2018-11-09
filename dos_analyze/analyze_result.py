from dos_analyze.dos_attribute import Dos_attribute


class Analyze_result():
    def __init__(self):
        self.map = dict()
        self.map[Dos_attribute.IS_IPV4] = 1

    def set_icmp(self):
        self.map[Dos_attribute.IS_ICMP] = 1

    def set_syn(self):
        self.map[Dos_attribute.IS_SYN] = 1

    def set_ack(self):
        self.map[Dos_attribute.IS_ACK] = 1

    def set_dns_in(self):
        self.map[Dos_attribute.IS_DNS_IN] = 1

    def set_dns_out(self):
        self.map[Dos_attribute.IS_DNS_OUT] = 1

    def set_key_exchange(self):
        self.map[Dos_attribute.IS_KEY_EXCHANGE] = 1

    def set_tls(self):
        self.map[Dos_attribute.IS_TLS] = 1

    def set_udp_length(self, length):
        self.map[Dos_attribute.UDP_LENGTH] = length

    def set_tcp_length(self, length):
        self.map[Dos_attribute.TCP_LENGTH] = length

    def set_ssh(self):
        self.map[Dos_attribute.IS_SSH] = 1

    def merge(self, other):
        for key in other.map:
            frequency = other.map[key]
            if key in self.map:
                self.map[key] += frequency
            else:
                self.map[key] = frequency

    def convertToList(self):
        result = []
        for attr in Dos_attribute.ATTRIBUTES:
            frequency = 0
            if attr in self.map:
                frequency = self.map[attr]
            result.append(frequency)
        return result
