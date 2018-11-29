from ml.neural_network import Neural_network
from ml.io_utils import load_data_test

data, label = load_data_test(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/data_for_testing_model/train")
data2, label2 = load_data_test(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/data_for_testing_model/test")

neural_network = Neural_network(len(data[0]), 10, 1)
neural_network.train(data, label, 200000,0.3)
hipo= neural_network.predict(data2)
for i in range(len(hipo)):
    print("{} - {} ".format(hipo[i],label2[i]))
