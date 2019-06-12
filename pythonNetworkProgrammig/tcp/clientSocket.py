from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 8889))
# s.send('GET /index.html HTTP/1.0n\n\n\n')
res = s.send('How are you'.encode('ascii'))
print(res)
data = s.recv(10000)
print(data)
s.close()

