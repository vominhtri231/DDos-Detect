from ml.io_utils import save_list_to_file


def reduce_attrs(data_pair, saved_train_file_name, saved_test_file_name):
    train_result = []
    test_result = []
    for file_name, label in data_pair:
        temp_result = []
        read_file = open(file_name, "r")
        label_result = create_label_result(label)
        for line in read_file:
            temp_result.append(create_attrs_result(line)+" " + label_result)
        temp_train_result, temp_test_result = divide_to_train_and_test(
            temp_result)
        train_result = train_result + temp_train_result
        test_result = test_result + temp_test_result
    save_list_to_file(saved_train_file_name, train_result)
    save_list_to_file(saved_test_file_name, test_result)


def create_attrs_result(line):
    attrs = line.split(";")
    attrs[-1] = attrs[-1][0:-1]
    reduced_attrs = attrs[0:5]+attrs[9:]
    return ";".join(reduced_attrs)


def create_label_result(label):
    full_lable = ['0']*5
    full_lable[label-1] = '1'
    return ";".join(full_lable)


def divide_to_train_and_test(origin_result):
    result_len = len(origin_result)
    threshold = int(result_len*0.8)
    return origin_result[0:threshold], origin_result[threshold:]


reduce_attrs([
    ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/normal.txt", 5],
    ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/ssh.txt", 4],
    ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/icmp.txt", 3],
    ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/udp.txt", 2],
    ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/syn.txt", 1]
], "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/train.txt",
    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/test.txt")
