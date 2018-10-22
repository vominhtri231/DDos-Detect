import struct


class Tls():
    HAND_SHAKE_TYPE = 22
    SERVER_KEY_EXCHANGE = 12
    CLIENT_KEY_EXCHANGE = 16

    def __init__(self, raw_data):
        self.type, self.version, self.length = struct.unpack(
            '! B H H', raw_data[:5])
        print(self.type)
        if self.is_hand_shake():
            self.handshake_type = struct.unpack('! B', raw_data[5])
            print(self.handshake_type)

    def is_hand_shake(self):
        return self.type == Tls.HAND_SHAKE_TYPE

    def is_key_exchange(self):
        return hasattr(self, 'handshake_type') and (
            self.handshake_type == Tls.SERVER_KEY_EXCHANGE or self.handshake_type == Tls.CLIENT_KEY_EXCHANGE)
