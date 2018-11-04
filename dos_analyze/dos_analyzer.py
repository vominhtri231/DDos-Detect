from network_packets.ethernet import Ethernet
from network_packets.ipv4 import Ipv4
from network_packets.icmp import Icmp
from network_packets.tcp import Tcp
from network_packets.udp import Udp
from network_packets.dns import Dns
from network_packets.tls import Tls
from dos_analyze.analyze_result import Analyze_result


def get_dos_info(raw_data, origin_ip):

    ether = Ethernet(raw_data)
    if ether.protocol == Ethernet.IPV4_PROTOCOL:
        ipv4 = Ipv4(ether.data)
        other_ip = ipv4.get_other_ip(origin_ip)
        result = Analyze_result()

        if ipv4.protocol == Ipv4.ICMP_PROTOCOL:
            result.set_icmp()
        elif ipv4.protocol == Ipv4.TCP_PROTOCOL:
            tcp = Tcp(ipv4.data)
            if tcp.is_using_ssh:
                result.set_ssh()
            if tcp.is_syn_only():
                result.set_syn()
            if tcp.is_ack_only():
                result.set_ack()
            if tcp.is_using_tls():
                tls = Tls(tcp.data)
                if tls.is_key_exchange():
                    result.set_key_exchange()
            result.set_tcp_length(tcp.length/1024)
            result.merge(get_dos_dns_info(tcp))
        elif ipv4.protocol == Ipv4.UDP_PROTOCOL:
            udp = Udp(ipv4.data)
            result.set_udp_length(udp.length/1024)
            result.merge(get_dos_dns_info(udp))

        return other_ip, result


def get_dos_dns_info(protocol):
    result = Analyze_result()
    if protocol.destination_port == 53:
        result.set_dns_out()
    if protocol.source_port == 53:
        result.set_dns_in()
    return result
