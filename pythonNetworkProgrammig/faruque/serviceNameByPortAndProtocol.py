import socket

def find_service_name():
	protocolname = 'tcp'

	for port in [i for i in range(1,100)]:

		try:
			print(port, 'Service name => ', socket.getservbyport(port, protocolname))
		except:
			print(port, 'No service running')
			continue

	print(53, 'Service => ', socket.getservbyport(53, 'udp'))

if __name__ == '__main__':
	find_service_name()