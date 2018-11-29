from os import listdir
from numpy import zeros, asarray


def load_data_test(dir_name):
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

        data[i, :] = one_file_data
        label[i] = int(files[i].split("_")[0])
    return data, label


def load_data(file_name):
    read_file = open(file_name, "r")
    list_data = []
    list_label = []
    for line in read_file:
        str_data_label = line.split(" ")
        data_as_int = [(float(ele)/1000.0)
                       for ele in str_data_label[0].split(";")]
        label_as_int = [(float(ele)) for ele in str_data_label[1].split(";")]
        list_data.append(asarray(data_as_int))
        list_label.append(asarray(label_as_int))
    return asarray(list_data), asarray(list_label)


def get_data_in_file(read_file):
    attrs = read_file.readlines()
    striped_attrs = [attr.strip("\n") for attr in attrs]
    line = ";".join(striped_attrs)
    return line+"\n"


def save_list_to_file(saved_file_name, saved_list):
    saved_file = open(saved_file_name, "a+")
    for line in saved_list:
        saved_file.write(line+"\n")
    saved_file.close()
