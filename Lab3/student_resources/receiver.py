import sys
import socket
import struct

group = sys.argv[1]
port = sys.argv[2]

#print("Group: ", group, "\tType: ", type(group))
#print("Port: ", port, "\t\tType: ", type(port))

HOST = group
PORT = int(port)

data_size = 9

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (HOST, PORT)
sock.bind(server_address)

group = socket.inet_aton(HOST)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    data = sock.recv(1024)
    #print('received %s bytes from %s' % (len(data), address))
    #print(data)
    text = data[6:].decode()
    print(text, flush=True)

while True:
	pass