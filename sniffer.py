import socket
from capture_traffic.network_packets.ethernet import Ethernet
from capture_traffic.network_packets.ipv4 import Ipv4
from capture_traffic.network_packets.icmp import Icmp
from capture_traffic.network_packets.tcp import Tcp
from capture_traffic.network_packets.udp import Udp


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        ether = Ethernet(raw_data)
        print("\n\n")
        print("Address : {}".format(addr))

        print("Ethernet || source : {} ,destination : {},protocol :{}".format(
            ether.source, ether.destination, ether.protocol))

        if ether.protocol == 8:
            ipv4 = Ipv4(ether.data)
            print("Ip || source : {} ,target : {},protocol :{}".format(
                ipv4.source, ipv4.target, ipv4.protocol))
            if ipv4.protocol == 1:
                icmp = Icmp(ipv4.data)
                print("ICMP || type:{}, code:{}, checksum:{}".format(
                    icmp.type, icmp.code, icmp.checksum))
            elif ipv4.protocol == 6:
                tcp = Tcp(ipv4.data)
                print("TCP || src_port:{},dst_port:{},seq={},ack={}".format(
                    tcp.source_port, tcp.destination_port, tcp.sequence, tcp.acknowledgment))
                print("TCP-Flag || urg:{},ack:{},psh={},rst={},syn={},fin={}".format(
                    tcp.flag_urg, tcp.flag_ack, tcp.flag_psh, tcp.flag_rst, tcp.flag_syn, tcp.flag_fin))
            elif ipv4.protocol == 17:
                udp = Udp(ipv4.data)
                print("UDP || src_port:{} ,dst_port:{}".format(
                    udp.source_port, udp.destination_port))


if __name__ == "__main__":
    main()
