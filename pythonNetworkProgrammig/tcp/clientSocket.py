from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('www.python.org', 80))
s.send('GET /index.html HTTP/1.0n\n\n\n')
data = s.recv(10000)
print(data)
s.close()

