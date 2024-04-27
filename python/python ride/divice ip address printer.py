import socket
hostname=socket.gethostname( )
ipAddr=socket.gethostbyname (hostname)
print("my ip address is "+ ipAddr)
print(hostname)
