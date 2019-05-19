import socket

def convert_integer():
	data = 1234

	#32bit
	print('original', data, ' Long host byte order ', socket.ntohl(data), ' long network by order ', socket.htonl(data))


	#16bit
	print('original', data, ' Long host byte order ', socket.ntohs(data), ' long network by order ', socket.htons(data))

if __name__ == '__main__':
	convert_integer()