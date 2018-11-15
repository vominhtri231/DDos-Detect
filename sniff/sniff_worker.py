import threading
from sniff.dos_analyze.dos_analyzer import get_dos_info
from sniff.dos_analyze.analyze_result import Analyze_result
from sniff.utils.get_ip import get_interface_ip


class Sniff_worker(threading.Thread):
    def __init__(self, conn, network_name):
        threading.Thread.__init__(self)
        self.conn = conn
        self.is_run = True
        self.network_name = network_name
        self.result = dict()

    def run(self):
        self_ip = get_interface_ip(self.network_name)
        while self.is_run:
            raw_data, addr = self.conn.recvfrom(65536)
            if addr[0] == self.network_name:
                res = get_dos_info(raw_data, self_ip)
                if res is not None:
                    other_ip, analyze_result = res
                    self.add_total_result(other_ip, analyze_result)

    def end_run(self):
        self.is_run = False

    def add_total_result(self, other_ip, analyze_result):
        if other_ip in self.result:
            self.result[other_ip].merge(analyze_result)
        else:
            self.result[other_ip] = analyze_result
