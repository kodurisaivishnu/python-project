import socket 

ip='10.36.230.128'
port=9993
ADDR=(ip,port)

FORMAT='utf-8'

SIZE=1024

def main():
	print("[STARTING]: server is starting...")
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen(5)
	print("[LISTINING]: server is started listining..")
	while True:
		conn,addr=server.accept()
		print(f"[NEW CONNECTION]: {addr} connected")
		
		filename=conn.recv(SIZE).decode(FORMAT)
		print(f"[RECV]: file name {filename} received")
		file=open(filename,'w')
		conn.send("[OK]:file name received..".encode(FORMAT))
		
		data=conn.recv(SIZE).decode(FORMAT)
		print(f"[RECV]: file data received..")
		file.write(data)
		conn.send("file completely received..".encode(FORMAT))
		file.close()
		conn.close()
		print(f"[DISCONNECTED]: {addr} is disconnected..")
		
		
if __name__=="__main__" :
	main()