from ftplib import FTP
import threading


class Request_sender(threading.Thread):
    def __init__(self, id, server_ip, path, file_name):
        threading.Thread.__init__(self)
        self.id = id
        self.server_ip = server_ip
        self.path = path
        self.file_name = file_name

    def run(self):
        file_parts = self.file_name.split(".")
        file_ext = file_parts[1]
        file_name_without_ext = file_parts[0]
        num = 1
        while(True):
            result_file_name = file_name_without_ext + \
                "_"+str(self.id)+"_"+str(num)+"."+file_ext
            result_path = "download_files/" + result_file_name
            self.send_request(result_path)
            num += 1

    def send_request(self, result_file_path):
        localFile = open(result_file_path, "wb")
        ftp = FTP(self.server_ip)
        ftp.login()
        ftp.cwd(self.path)
        ftp.retrbinary("RETR "+self.file_name, localFile.write)
        localFile.close()
        ftp.quit()
