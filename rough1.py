from random import getrandbits
from ipaddress import IPv4Address

bits = getrandbits(32)
print bits
addr = IPv4Address(bits)
str_addr =  str(addr)



filename = datetime.datetime.now().strftime(filename_suffix)
file = open("%s_%s.txt" % (filename_prefix,filename), "w")


file = open("{0}_{1}.txt".(filename_prefix,filename), "w")


with open("config.ini") as f:
    sample_config = f.read()
    config = configparser.ConfigParser()
    config.read_string(sample_config)
    write_log_files(int(config['log_generator']['num_of_files']),int(config['log_generator']['num_of_lines']))
