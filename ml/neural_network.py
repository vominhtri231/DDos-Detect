from numpy import exp, log, dot, zeros, shape, transpose, c_, ones, random
from math import sqrt
import pickle


class Neural_network:
    number_file = "number.txt"
    weight1_file = "weight1.txt"
    weight2_file = "weight2.txt"

    def __init__(self, n, hidden_node_numbers=None, output_numbers=None):
        if hidden_node_numbers == None or output_numbers == None:
            self.__init_with_dir(n)
        else:
            self.__init_with_node_number(n, hidden_node_numbers, output_numbers)

    def __init_with_dir(self, dir_path):
        self.__get_num_in_file(dir_path+"/"+Neural_network.number_file)
        self.weigh1 = self.__get_array_in_file(
            dir_path+"/"+Neural_network.weight1_file)
        self.weigh2 = self.__get_array_in_file(
            dir_path+"/"+Neural_network.weight2_file)

    def __init_with_node_number(self, n, hidden_node_number, output_number):
        self.n = n
        self.hidden_node_number = hidden_node_number
        self.output_number = output_number
        self.weigh1 = self.__init_random_mat(n+1, self.hidden_node_number)
        self.weigh2 = self.__init_random_mat(
            self.hidden_node_number+1, output_number)

    def train(self, data, label, times, alpha):
        m = len(data)
        for i in range(times):
            self.__grad_decent(data, label, alpha)

    def predict(self, data):
        m = len(data)
        data = c_[ones((m, 1)), data]
        a2 = self.__sigmoid(dot(data, self.weigh1))
        a2 = c_[ones((m, 1)), a2]
        return self.__sigmoid(dot(a2, self.weigh2))

    def save_state(self, dir_path):
        self.__save_num_in_file(dir_path+"/"+Neural_network.number_file)
        self.__save_array_in_file(
            self.weigh1, dir_path+"/"+Neural_network.weight1_file)
        self.__save_array_in_file(
            self.weigh2, dir_path+"/"+Neural_network.weight2_file)

    def __grad_decent(self, data, label, alpha):
        m = len(data)
        data = c_[ones((m, 1)), data]
        z2 = dot(data, self.weigh1)
        a2 = self.__sigmoid(z2)
        a2 = c_[ones((m, 1)), a2]
        z3 = dot(a2, self.weigh2)
        a3 = self.__sigmoid(z3)

        print(self.__lost_value(a3, label))

        delta3 = a3 - label
        delta2 = dot(delta3, self.weigh2.transpose())[
            :, 1:] * self.__sigmoid_derivative(z2)
        self.weigh2 -= dot(a2.transpose(), delta3)/m*alpha
        self.weigh1 -= dot(data.transpose(), delta2)/m*alpha

    def __sigmoid(self, x):
        return 1/(1+exp(-x))

    def __sigmoid_derivative(self, x):
        return self.__sigmoid(x)*(1-self.__sigmoid(x))

    def __lost_value(self, predict_value, label):
        error = label*log(predict_value) + (1-label)*log(1-predict_value)
        return error.sum()*-1/len(label)

    def __init_random_mat(self, n, m):
        epsilon = sqrt(6)/sqrt(m+n)
        res = random.random((n, m))
        res = res*2*epsilon
        return res-epsilon

    def __save_array_in_file(self, saved_array, saved_file_name):
        with open(saved_file_name, 'wb') as fp:
            pickle.dump(saved_array, fp)

    def __get_array_in_file(self, saved_file_name):
        with open(saved_file_name, "rb") as fp:
            return pickle.load(fp)

    def __save_num_in_file(self, saved_file_name):
        saved_file = open(saved_file_name, "w+")
        saved_file.write(str(self.n)+"\n")
        saved_file.write(str(self.hidden_node_number)+"\n")
        saved_file.write(str(self.output_number)+"\n")
        saved_file.close()

    def __get_num_in_file(self, saved_file_name):
        saved_file = open(saved_file_name, "r")
        lines = saved_file.readlines()
        self.n = int(lines[0])
        self.hidden_node_number = int(lines[1])
        self.output_number = int(lines[2])
        saved_file.close()
