import socket as sock  # An API for socket
import os
import sub
def echo():
    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            data = data.decode().strip()
            print("Data from {} : {} [for echo]".format(addr[0], data))
            if (data == "quit" or data == "exit"):
                conn.sendall("Connection closed to echo..\n".encode())
                break
            else:
                data = "echo >>" + data + "\n"
                conn.sendall(data.encode())

def cmd():
    conn.sendall("--------------------\n".encode())
    while True:
        conn.sendall("cmd >>>".encode())
        data = conn.recv(1024)
        if not data:
            break
        else:
            data = data.decode().strip()
            print("Data from {} : {} [For cmd]".format(addr[0], data))
            if (data == "quit" or data == "exit"):
                conn.sendall("Connection closed to cmd..\n".encode())
                break
            else:
                """proc = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()"""
                try:
                    result=os.popen(data).read()
                    result = "\nYour output:\n" + result
                    conn.sendall(result.encode())
                except:
                    conn.sendall("Invalid Command [Note:This server accepts only windows cmd!\n".encode())


host=""
port=4444

s=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.bind((host,port))
s.listen(100)
conn,addr=s.accept()
print("{} is connected with back port {}".format(addr[0],addr[1]))
while True:
    conn.sendall("\nChoose from the following :\n1.echo\n2.cmd\nYour choice:".encode())
    data=conn.recv(1024)
    if not data:
        break
    else:
        data=data.decode().strip()
        print("Data from {} : {}".format(addr[0],data))
        if (data=="quit" or data=="exit"):
            conn.sendall("Connection closed ..\n".encode())
            break
        elif(data=="1"):
            echo()
            continue
        elif(data=="2"):
            cmd()
        else:
            pass

s.close()
