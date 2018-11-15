from ftplib import FTP
import threading


class Request_sender(threading.Thread):
    def __init__(self, id, server_ip, username, password, path, file_name):
        threading.Thread.__init__(self)
        self.id = id
        self.server_ip = server_ip
        self.username = username
        self.password = password
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
            self.send_request("download_files/" + result_file_name)
            num += 1

    def send_request(self, result_file_path):
        ftp = FTP(self.server_ip)
        ftp.login(self.username, self.password)
        ftp.cwd(self.path)
        ftp.retrbinary("RETR "+self.file_name,
                       open(result_file_path, "wb").write)
        ftp.quit()
