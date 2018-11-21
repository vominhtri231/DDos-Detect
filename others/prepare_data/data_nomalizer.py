import glob
import os


def normalize_data(folder_path, stored_file_path, target_ip):
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        read_file = open(file_name, "r")
        ip = read_file.readline().rstrip()
        if ip == target_ip:
            stored_file = open(stored_file_path, "a+")
            line = get_data_in_file(read_file)
            stored_file.write(line)
            stored_file.close()
        read_file.close()


def get_data_in_file(read_file):
    attrs = read_file.readlines()
    striped_attrs = [attr.strip("\n") for attr in attrs]
    line = ";".join(striped_attrs)
    return line+"\n"
