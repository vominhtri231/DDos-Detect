class Dos_attribute():
    IS_IPV4 = "is_ipv4"
    IS_ICMP = "is_icmp"
    IS_SYN = "is_syn"
    IS_ACK = "is_ack"
    IS_DNS_IN = "is_dns_out"
    IS_DNS_OUT = "is_dns_in"
    IS_KEY_EXCHANGE = "is_key_exchange"
    IS_TLS = "is_tls"
    IS_SSH = "is_ssh"
    TCP_LENGTH = "tcp_length"
    UDP_LENGTH = "udp_length"
    ATTRIBUTES = [IS_IPV4, IS_ICMP, IS_SYN, IS_ACK, IS_SSH,
                  UDP_LENGTH, TCP_LENGTH]
   #IS_DNS_IN,  IS_DNS_OUT, IS_KEY_EXCHANGE, IS_TLS is removed
