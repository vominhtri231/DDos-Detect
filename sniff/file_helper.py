from dos_analyze.analyze_result import Analyze_result


def save_to_file(filepath, ip, result: Analyze_result):
    f = open(filepath, "w")
    f.write(ip+"\n")
    list_feature = result.convertToList()
    for feature in list_feature:
        f.write(str(feature)+"\n")
    f.close()


def save_result_in_folder(ip, result: Analyze_result):
    filePath = "{}/{}.txt".format(save_result_in_folder.folder_path,
                                  save_result_in_folder.index)
    save_to_file(filePath,ip, result)
    save_result_in_folder.index += 1


save_result_in_folder.folder_path = "/home/minhtri/Code-workspae/python-workspace/DDosDetect/data/ssh"
save_result_in_folder.index = 0
