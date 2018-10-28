from os import listdir
from numpy import zeros


def load_data(dir_name):
    files = listdir(dir_name)
    m = len(files)
    data = zeros((m, 1024))
    label = zeros((m, 1))

    for i in range(m):
        one_file_data = zeros((1, 1024))
        file_name = "{}/{}".format(dir_name, files[i])

        f = open(file_name, "r")
        for j in range(32):
            line = f.readline()
            for k in range(32):
                one_file_data[0, 32*j+k] = int(line[k])
        
        data[i,:] = one_file_data
        label[i] = int(files[i].split("_")[0])
    return data,label
