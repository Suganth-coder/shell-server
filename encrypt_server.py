from cryptography.fernet import Fernet
import socket as sock  # An API for socket
import os
import subprocess

def lis_to_str(lis):
    string=""
    for i in lis:
        string=string+str(i)
    return string

def add_salt(data):
    lis=[]
    inc=5
    for i in data:
        temp=ord(i)+inc
        lis.append(chr(temp))

        if inc>20:
            inc=inc-5

    string=lis_to_str(lis)
    return string

def data_check(data):
    if data==None:
        conn.sendall("Invalid data".encode())

def encrypt(data):

    original_data=data
    data=add_salt(data)
    print("Data after added salt:{}".format(data))
    key=Fernet.generate_key()
    fer=Fernet(key)
    j="temporary"
    with open("result.txt",'a') as res:
        temp="Output {}:\n\n{}".format(j,original_data)
        res.write(temp)

    with open("result.txt",'rb') as en:
        token=fer.encrypt(en.read())
        return key,token

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
        if data=='\r\n'.encode():
            count1 = myfunc()
            if count1 <=4:
                conn.sendall("\n----Please Enter the command!...----\n".encode())
            else:
                conn.sendall("\n --You have reached maximum attempts!--\n".encode())
                break
            print(count1)
        else:
            try:
                data = data.decode().strip()
                print("Data from {} : {} [For cmd]".format(addr[0], data))
            except:
                print("\n$$ Data is not decoded [In cmd] $$")
            if (data == "quit" or data == "exit"):
                conn.sendall("Connection closed to cmd..\n".encode())
                break
            elif data==None:
                data_check(data)
            else:
                try:
                    result=os.popen(data).read()
                    result = "\nYour output:\n" + result
                    key,result=encrypt(result)
                    conn.sendall(result)
                except:
                    conn.sendall("Invalid Command [Note:This server accepts only windows cmd!]\n".encode())

def myfunc():
    myfunc.counter += 1
    return myfunc.counter

myfunc.counter = 0

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

    try:
        data = data.decode().strip()
        print(data)
    except:
        print("Data is not decoded")

    if not data:
        count1=myfunc()
        if count1<=3:
            conn.sendall("\n----Data is not entered!...----\n".encode())
        else:
            conn.sendall("\n --You have reached maximum attempts!--\n".encode())
            break
        print(count1)
    else:

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
