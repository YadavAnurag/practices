import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8888))
s.listen(5)

while True:
	try:
		c, addr = s.accept()
		buf = s.recv(2048)
		if not len(buf):
			print('No data')
			sys.exit(1)
	except socket.error as e:
		print('error while receving data')
	

