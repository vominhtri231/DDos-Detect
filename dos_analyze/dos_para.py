
def enum(**enums):
    return type('Enum', (), enums)


Dos_para = enum(IS_ICMP="is_icmp",
                IS_SYN="is_syn",
                IS_ACK="is_ack",
                IS_DNS_IN="is_dns_out",
                IS_DNS_OUT="is_dns_in")
