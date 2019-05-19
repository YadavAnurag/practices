import socket
import sys
import argparse


def main():
	parser = argparse.ArgumentParser(description= 'Socket error example')

	parser.add_argument('--host', action='store', dest="host", required=False)
	parser.add_argument('--port', action='store', dest='port', required=False)
	parser.add_argument('--file', action='store', dest='file', required=False)

	given_args = parser.parse_args()

	host = given_args.host
	port = int(given_args.port)
	filename = given_args.file 

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as e:
		print('Error creating socket', e)
		sys.exit(1)

	try:
		s.connect((host, port))
	except socket.gaierror as e:
		print('Address related error connecting to socket.....')
		sys.exit(1)
	except socket.error as e:
		print('Connecting.......')
		sys.exit(1)


	try:
		msg = 'GET %s HTTP/1.0\r\n\r\n' %filename
		s.sendall(msg.encode('utf-8'))
	except socket.error as e:
		print('Error while sending data', e)
		sys.exit(1)

	while True:
		try:
			buf = s.recv(2048)
		except socket.error as e:
			print('Error receiving data',e)
			sys.exit(1)
		if not let(buf):
			break

if __name__ == '__main__':
	main()

