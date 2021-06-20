import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.hackucf.org', 10101))
data = s.recv(100)
data = s.recv(44)
while 1:
    data = s.recv(1024)
    st = data.decode("utf-8")
    print(st)
    print(st[st.find(' ')+1:st.find('\n')])
    s.sendall(st[st.find(' ')+1:st.find('\n')+1].encode())