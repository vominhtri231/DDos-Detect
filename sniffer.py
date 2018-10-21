import socket
from capture_traffic.network_packets.ethernet import Ethernet
from capture_traffic.network_packets.ipv4 import Ipv4
from capture_traffic.network_packets.icmp import Icmp
from capture_traffic.network_packets.tcp import Tcp
from capture_traffic.network_packets.udp import Udp
from capture_traffic.network_packets.dns import Dns


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        ether = Ethernet(raw_data)
        print("\n")
        print("Address : {}".format(addr))

        ether.get_info()

        if ether.protocol == 8:
            ipv4 = Ipv4(ether.data)
            ipv4.get_info()
            if ipv4.protocol == 1:
                icmp = Icmp(ipv4.data)
                icmp.get_info()
            elif ipv4.protocol == 6:
                tcp = Tcp(ipv4.data)
                tcp.get_info()
                if tcp.destination_port == 53 or tcp.source_port == 53:
                    sniff_dns(tcp.data)
                elif tcp.source_port == 22 or tcp.destination_port == 22:
                    sniff_ssh(tcp.data)

            elif ipv4.protocol == 17:
                udp = Udp(ipv4.data)
                udp.get_info()
                if udp.destination_port == 53 or udp.source_port == 53:
                    sniff_dns(udp.data)


def sniff_dns(raw_data):
    if len(raw_data) > 12:
        dns = Dns(raw_data)
        dns.get_info()

def sniff_ssh(raw_data):
    print("not yet")


if __name__ == "__main__":
    main()
