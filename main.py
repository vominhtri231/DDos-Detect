from sniff.sniff_manager import Sniff_Manager
from ml.neural_network import Neural_network
import ml.const
from numpy import argmax, transpose, asarray, shape, zeros
from gui.main_screen import Main_screen


def handle_result(result):
    statistic_result = [0, 0, 0]
    warning_results = []
    for address in result:
        data = result[address].convertToList()
        statistic_result[0] += data[0]
        statistic_result[1] += data[5]
        statistic_result[2] += data[6]

        input_data = convert_sniff_result(data)
        hipo = neural_network.predict(input_data)
        index = hipo[0].argmax()
        print("{},{}".format(index, hipo[0][index]))

        warning_results.append(
            ((address, ml.const.dos_labels[index], hipo[0][index]),
             index != ml.const.normal))
    screen.update(statistic_result, warning_results)


def convert_sniff_result(data):
    normalized_data = [ele/1000.0 for ele in data]
    input_data = zeros((1, 7))
    for i in range(7):
        input_data[0][i] = normalized_data[i]
    return input_data


neural_network = Neural_network(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/saved_neural_network_state")
screen = Main_screen()
manager = Sniff_Manager(10, "wlp3s0", handle_result)
manager.start()
screen.mainloop()
