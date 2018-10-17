import socket
from capture_traffic.network_packets.ethernet import Ethernet
from capture_traffic.network_packets.ipv4 import Ipv4


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        ether = Ethernet(raw_data)
        print("Address : {}".format(addr))

        print("Ethernet : source : {} ,destination : {},prototype :{}".format(
            ether.source, ether.destination, ether.prototype))

        ipv4 = Ipv4(ether.data)
        print("Ip : source : {} ,destination : {},protocol :{},version:{}".format(
            ipv4.src, ipv4.target, ipv4.prototocol, ipv4.version))


if __name__ == "__main__":
    main()
