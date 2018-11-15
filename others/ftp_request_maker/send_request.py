from utils.ftp_request_maker.request_sender import Request_sender


def start_send_request():
    ip = "192.168.1.3"
    username = "tri"
    password = "vominhtri"
    path = ""
    file_name = "friend-ss1.zip"
    Request_sender(1, ip, username, password, path, file_name).start()
    Request_sender(2, ip, username, password, path, file_name).start()


if __name__ == "__main__":
    start_send_request()
