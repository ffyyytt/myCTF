import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.hackucf.org', 10102))
data = s.recv(100)
data = s.recv(44)
flag = 0
l = []

while 1:
    data = s.recv(1024)
    st = data.decode("utf-8")
    print(st)
    print('-------END-------')
    if ('Good' in st):
        flag = 1
    if (flag == 0):
        l.append(st[st.find(' ')+1:st.find('\n')+1])
        s.sendall(st[st.find(' ')+1:st.find('\n')+1].encode())
    else:
        s.sendall(l[0].encode())

