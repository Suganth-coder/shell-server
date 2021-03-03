import socket as sock

host="127.0.0.1"
port=4444
s=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.connect((host,port))

while True:
    data=s.recv(1024)
    print("{}".format(data.decode()))
    inp = input("To Server:")
    if inp=="end":
        break
    s.sendall(inp.encode())



