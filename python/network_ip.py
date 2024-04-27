import socket
def get_network_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("divice ip: ",socket.gethostbyname('localhost'))
    s.connect(('8.8.8.8',1))
    ip_address=s.getsockname()[0]
    s.close()
    return ip_address
print("Network ip Address: ",get_network_ip())


#vartion_2
'''from socket import *
def ip():
    s=socket(AF_INET,SOCK_DGRAM)
    s.connect('8.8.8.8',1)
    return s.getsockname()[0]
print("ip=",ip())
'''