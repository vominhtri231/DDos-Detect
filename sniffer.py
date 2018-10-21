import socket
from dos_analyze.dos_analyzer import Dos_analyzer


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        print("\n")
        print("Address : {}".format(addr))
        dos_analyzer = Dos_analyzer(raw_data)
        dos_analyzer.get_result()


if __name__ == "__main__":
    main()
