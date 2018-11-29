import socket
import time
from numpy import argmax, transpose, asarray, shape, zeros
from sniff.sniff_worker import Sniff_worker
from sniff.utils.save_sniff_result import save_result_in_folder
from ml.neural_network import Neural_network


class Sniff_Manager():
    def __init__(self, time_period, network_name):
        self.time_period = time_period
        self.network_name = network_name
        self.neural_network = Neural_network(
            "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/saved_neural_network_state")

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
        for key in result:
            data = result[key].convertToList()
            input_data = self.__convert_sniff_result(data)
            hipo = self.neural_network.predict(input_data)
            index = hipo[0].argmax()
            print("{},{}".format(index, hipo[0][index]))
            # save_result_in_folder(key, result[key])


    def __convert_sniff_result(self, data):
        normalized_data=[ele/1000.0 for ele in data]
        input_data=zeros((1, 7))
        for i in range(7):
            input_data[0][i]=normalized_data[i]
        return input_data
