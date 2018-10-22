import socket
import time
from sniff.sniff_worker import Sniff_worker


class Sniff_Manager():
    def __init__(self, time_period, network_name):
        self.time_period = time_period
        self.network_name = network_name
        self.results = []

    def start_sniff(self):
        conn = socket.socket(
            socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        while True:
            worker = Sniff_worker(conn, self.network_name)
            worker.start()
            time.sleep(self.time_period)
            worker.end_run()
            self.handle_result(worker.result)

    def handle_result(self, result):
        self.results.append(result)
        print(result.map)
