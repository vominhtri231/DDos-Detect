from ml.sigmoid_regression import gradDecent, predict, add_bias
from ml.io_utils import load_data_test
from numpy import shape

data, label = load_data_test(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/data_for_testing_model/train")
data2, label2 = load_data_test(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/data_for_testing_model/test")

data = add_bias(data)
weigh = gradDecent(data, label, 1, 10000)

data2 = add_bias(data2)
hipo = predict(data2, weigh)
for i in range(len(hipo)):
    print("{} - {} ".format(hipo[i], label2[i]))
