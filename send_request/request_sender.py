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
        file_parts = file_name.split(".")
        self.file_ext = file_parts[1]
        self.file_name_without_ext = file_parts[0]

    def run(self):
        num = 1
        while(True):
            file_name = self.file_name_without_ext+str(num)+"."+self.file_ext
            self.send_request("download_files/"+str(self.id)+"/" + file_name)
            num += 1

    def send_request(self, result_file_name):
        ftp = FTP(self.server_ip)
        ftp.login(self.username, self.password)
        ftp.cwd(self.path)
        ftp.retrbinary("RETR "+self.file_name_without_ext+"."+self.file_ext,
                       open(result_file_name, "wb").write)
        ftp.quit()
