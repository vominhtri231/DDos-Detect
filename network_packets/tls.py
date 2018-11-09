import struct


class Tls():
    HAND_SHAKE_TYPE = 22
    SERVER_KEY_EXCHANGE = 12
    CLIENT_KEY_EXCHANGE = 16

    def __init__(self, raw_data):
        if raw_data:
            self.type = raw_data[0]
            if self.is_hand_shake():
                self.handshake_type = raw_data[5]

    def is_hand_shake(self):
        return self.type == Tls.HAND_SHAKE_TYPE

    def is_key_exchange(self):
        return hasattr(self, 'handshake_type') and (
            self.handshake_type == Tls.SERVER_KEY_EXCHANGE or self.handshake_type == Tls.CLIENT_KEY_EXCHANGE)
