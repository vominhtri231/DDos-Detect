from ml.prepare_data.io_utils import save_list_to_file


def reduce_attrs(data_pair, saved_file_name):
    result = []
    for file_name, label in data_pair:
        read_file = open(file_name, "r")
        label_result = create_label_result(label)
        for line in read_file:
            result.append(create_attrs_result(line)+" " + label_result)
    save_list_to_file(saved_file_name, result)


def create_attrs_result(line):
    attrs = line.split(";")
    attrs[-1] = attrs[-1][0:-1]
    reduced_attrs = attrs[0:5]+attrs[9:]
    return ";".join(reduced_attrs)


def create_label_result(label):
    full_lable = ['0']*5
    full_lable[label-1] = '1'
    return ";".join(full_lable)

#  reduce_attrs([
#         ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/normal.txt", 5],
#         ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/ssh.txt", 4],
#         ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/icmp.txt", 3],
#         ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/udp.txt", 2],
#         ["/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/syn.txt", 1]
#     ],"/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/final_input.txt")