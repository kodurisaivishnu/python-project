import socket

ip=socket.gethostbyname(socket.gethostname())

port=9999

ADDR=(ip,port)

FORMAT='utf-8'

SIZE=1024

def main():
	client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(ADDR)
	file=open("python ride/harish1.py",'r')
	data=file.read()
	client.send("harish1.py".encode(FORMAT))
	msg=client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
	
	client.send(data.encode(FORMAT))
	msg=client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
	file.close()
	client.close()
	

if __name__=="__main__" :
	main()