import sys
import socket

server = sys.argv[1]
port = sys.argv[2]
cmd = sys.argv[3]

#print("Server: ", server, "Type: ", type(server))
#print("Port: ", port, "Type: ", type(port))
#print("Command: ", cmd, "Type: ", type(cmd))


HOST = server
PORT = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

#print("sending:", cmd)
sock.sendall(cmd.encode())
	
received = 0
received_old = -1
acc = 0
# Max 90 messages are sent
expected = 90*19
data_size = 18
counter = 0

#while True:
while received < expected:
    counter += 1
    data = sock.recv(data_size).decode()
    received += len(data)
    if(len(data) > 0):
        print (data, flush=True)
    
    # Save current state of the received buffer size
    if received_old == received:
        acc += 1
        # If nothing is received after 5 iterations, break
        if acc == 5:
            break
    received_old = received
    if counter == 10:
        data_size += 1
    

while True:
	pass
