import struct


class Dns():
    def __init__(self, raw_data):
        self.id, self.flag, self.question_count, self.result_count, self.author_record_count, self.add_record_count = struct.unpack(
            "! 2s 2s H H H H", raw_data[:12])

    def get_info(self):
        print("DNS : question:={}, answer:{} , auth:{} ,addition:{}".format(
            self.question_count, self.result_count, self.author_record_count, self.add_record_count))
