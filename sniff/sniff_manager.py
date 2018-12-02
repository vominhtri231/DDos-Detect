import socket
import time
import threading
from sniff.sniff_worker import Sniff_worker


class Sniff_Manager(threading.Thread):
    def __init__(self, time_period, network_name, handle_result_function):
        threading.Thread.__init__(self)
        self.time_period = time_period
        self.network_name = network_name
        self.handle_result_function = handle_result_function

    def run(self):
        conn = socket.socket(
            socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        while True:
            worker = Sniff_worker(conn, self.network_name)
            worker.start()
            time.sleep(self.time_period)
            worker.end_run()
            self.handle_result_function(worker.result)
