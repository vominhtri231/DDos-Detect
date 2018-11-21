from others.ftp_request_maker.request_sender import Request_sender


def start_send_request():
    ip = "192.168.3.47"
    path = ""
    file_name = "friend-ss1.zip"
    Request_sender(1, ip, path, file_name).start()


if __name__ == "__main__":
    start_send_request()
