import glob
import os
from ml.prepare_data.io_utils import get_data_in_file,save_list_to_file

def normalize_data(folder_path, stored_file_path, target_ip):
    result = []
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        read_file = open(file_name, "r")
        ip = read_file.readline().rstrip()
        if ip == target_ip:
            line = get_data_in_file(read_file)
            result.append(line)
        read_file.close()
    save_list_to_file(stored_file_path,result)

# normalize_data("/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normal",
#                    "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/normalized_data/normal.txt",
#                    "192.168.1.2")