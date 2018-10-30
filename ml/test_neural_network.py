from neural_network import Neural_network
from os_heplder import load_data

data, label = load_data(
    "/Users/mba0066/code-workspace/python-workspace/DDos detect/data/train")
data2, label2 = load_data(
    "/Users/mba0066/code-workspace/python-workspace/DDos detect/data/test")

neural_network = Neural_network(len(data[0]), 10, 1)
neural_network.train(data, label, 10000,1)
hipo= neural_network.predict(data2)
for i in range(len(hipo)):
    print("{} - {} ".format(hipo[i],label2[i]))
