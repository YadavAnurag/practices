import socket


hostname = socket.gethostname()
print(hostname, socket.gethostbyname(hostname))
