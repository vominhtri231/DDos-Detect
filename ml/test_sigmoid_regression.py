from sigmoid_regression import gradDecent, predict, add_bias
from os_heplder import load_data
from numpy import shape

data, label = load_data(
    "/Users/mba0066/code-workspace/python-workspace/DDos detect/data/train")
data2, label2 = load_data(
    "/Users/mba0066/code-workspace/python-workspace/DDos detect/data/test")

data = add_bias(data)
weigh = gradDecent(data, label, 1, 10000)

data2 = add_bias(data2)
hipo = predict(data2, weigh)
for i in range(len(hipo)):
    print("{} - {} ".format(hipo[i], label2[i]))
