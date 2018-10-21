from network_packets.ethernet import Ethernet
from network_packets.ipv4 import Ipv4
from network_packets.icmp import Icmp
from network_packets.tcp import Tcp
from network_packets.udp import Udp
from network_packets.dns import Dns
from dos_analyze.analyze_result import Analyze_result

class Dos_analyzer():
    def __init__(self, raw_data):
        self.result = Analyze_result()
        ether = Ethernet(raw_data)
        if ether.protocol == Ethernet.IPV4_PROTOCOL:
            ipv4 = Ipv4(ether.data)
            if ipv4.protocol == Ipv4.ICMP_PROTOCOL:
                self.result.set_icmp()
            elif ipv4.protocol == Ipv4.TCP_PROTOCOL:
                tcp = Tcp(ipv4.data)
                if tcp.is_syn_only():
                    self.result.set_syn()
                if tcp.is_ack_only():
                    self.result.set_ack()
                self.check_dns(tcp)
            elif ipv4.protocol == Ipv4.UDP_PROTOCOL:
                udp = Udp(ipv4.data)
                self.check_dns(udp)

    def check_dns(self, protocol):
        if protocol.destination_port == 53:
            self.result.set_dns_out()
        if protocol.source_port == 53:
            self.result.set_dns_in()
    
    def get_result(self):
        print(self.result.values)
