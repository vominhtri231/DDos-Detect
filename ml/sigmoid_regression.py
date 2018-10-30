from numpy import exp, ones, shape, log, c_, zeros, dot


def sigmoid(x):
    return 1.0/(1+exp(-x))


def predict(data, weigh):
    return sigmoid(dot(data, weigh))


def add_bias(data):
    m = len(data)
    return c_[ones((m, 1)), data]


def gradDecent(data, label, alpha, max):
    m, n = shape(data)
    weigh = zeros((n, 1))

    for i in range(max):
        hipo = predict(data, weigh)
        print(lostFunction(hipo, label))
        error = hipo - label
        weigh = weigh - alpha*dot(data.transpose(), error)/m
    return weigh


def lostFunction(hipo, label):
    m = len(label)
    possitive_error = label * log(hipo)
    negative_error = (1-label) * log(1-hipo)
    error = negative_error + possitive_error
    return error.sum()*-1.0/m
