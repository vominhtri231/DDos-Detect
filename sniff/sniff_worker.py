import threading
from dos_analyze.dos_analyzer import get_dos_info
from dos_analyze.analyze_result import Analyze_result


class Sniff_worker(threading.Thread):
    def __init__(self, conn, network_name):
        threading.Thread.__init__(self)
        self.conn = conn
        self.is_run = True
        self.network_name = network_name
        self.result = Analyze_result()

    def run(self):
        while self.is_run:
            raw_data, addr = self.conn.recvfrom(65536)
            if addr[0] == self.network_name:
                self.result.merge(get_dos_info(raw_data))

    def end_run(self):
        self.is_run = False
