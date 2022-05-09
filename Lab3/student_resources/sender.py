import sys
import socket
import struct

group = sys.argv[1]
port = sys.argv[2]
sciper = sys.argv[3]

#print("Group: ", group, "\tType: ", type(group))
#print("Port: ", port, "\t\tType: ", type(port))

GROUP = group
PORT = int(port)
SCIPER = sciper

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (GROUP, PORT)

while True:
    user_input = input()
    text = SCIPER + user_input
    sock.sendto(text.encode(), server_address)

while True:
	pass