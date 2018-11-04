from numpy import exp, log, dot, zeros, shape, transpose, c_, ones, random
from math import sqrt


class Neural_network:
    def __init__(self, n, hide_node_numbers, output_numbers):
        self.n = n
        self.hide_node_numbers = hide_node_numbers
        self.output_numbers = output_numbers
        self.weigh1 = self.__init_random_mat(n+1, self.hide_node_numbers)
        self.weigh2 = self.__init_random_mat(
            self.hide_node_numbers+1, output_numbers)

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
