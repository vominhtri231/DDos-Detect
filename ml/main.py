from ml.neural_network import Neural_network
from ml.io_utils import load_data
from numpy import argmax

data, label = load_data(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/train.txt")
data2, label2 = load_data(
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/test.txt")
saved_state_dir = "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/saved_neural_network_state"
# neural_network = Neural_network(7, 10, 5)
# neural_network.train(data, label, 10000, 3)
# neural_network.save_state(saved_state_dir)



# hipo = neural_network.predict(data2)
# for i in range(len(hipo)):
#     print("{} - {} ".format(hipo[i], label2[i]))


recover_neural_network = Neural_network(saved_state_dir)

# recover_neural_network.train(data, label, 50000, 3)
# recover_neural_network.save_state(saved_state_dir)

hipo = recover_neural_network.predict(data2)
r_a = 0
f_a =0
for i in range(len(hipo)):
    j = hipo[i].argmax()
    k = label2[i].argmax()
    if j == k :
        r_a +=1
    else :
        f_a +=1
    
print("{} - {} ".format(r_a, f_a))

