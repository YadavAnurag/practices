import socket

def get_socket_timeout():
	tempSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	print('Default socket timeout', tempSocket.gettimeout())
	tempSocket.settimeout(100)
	print(tempSocket.gettimeout())


if __name__ == '__main__':
	get_socket_timeout()