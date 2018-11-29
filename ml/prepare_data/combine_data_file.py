import glob
import os
from ml.io_utils import get_data_in_file, save_list_to_file


def normalize_data(folder_path, stored_file_path, target_ip):
    result = []
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        read_file = open(file_name, "r")
        ip = read_file.readline().rstrip()
        if target_ip != "" and ip != target_ip:
            continue
        line = get_data_in_file(read_file)
        result.append(line)
        read_file.close()
    save_list_to_file(stored_file_path, result)


normalize_data("/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normal",
               "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/normal.txt",
               "")
