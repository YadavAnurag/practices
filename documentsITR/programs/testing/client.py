import socket
 
HOST = "127.0.0.1"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall("Hello\n".encode())
data = sock.recv(1024)
print (data)
 
if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    data = sock.recv(1024)
    print(data)

 
    if (data == "eyB}\n"):
        sock.close()
        print ("Socket closed")