import socket

def get_remote_machine_info():
	hostname = socket.gethostname()
	domainname = 'www.mmmut.ac.in'
	try:
		print('ip of {} is {}'.format(domainname, socket.gethostbyname(domainname)))
	except socket.error as err:
		print('ip of {} is {}'.format(hostname, err))

if __name__ == '__main__':
	get_remote_machine_info()