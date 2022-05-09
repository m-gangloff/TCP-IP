import sys
import socket

server = sys.argv[1]
port = sys.argv[2]

#print("Server: ", server, "Type: ", type(server))
#print("Port: ", port, "Type: ", type(port))

HOST = server
PORT = int(port)
cmd = "RESET:20"
data_size = 9

def send_reset(s_type=socket.AF_INET):
    try:
        sock = socket.socket(s_type, socket.SOCK_DGRAM)

        sock.settimeout(1)

        sock.sendto(cmd.encode(), (HOST,PORT))

        data, _ = sock.recvfrom(data_size)
        data = data.decode()

        sock.close()

        if data:
            return data

    except:
        sock.close()


counter_sum = 0
for i in range(60):
    ack_received = False
    counter = 0
    while not ack_received:
        data = send_reset(socket.AF_INET)
        data6 = send_reset(socket.AF_INET6)
        #print("Iteration number :", counter, "\t\tData_v4 :", data, "\t\tData_v6 :", data6)
        counter += 1
        if (data != None and (len(data) > 0)) or (data6 != None and (len(data6) > 0)):
            ack_received = True
    counter_sum += counter
    print("Iteration ", i, " has counter: ", counter)

average = counter_sum/60
print(average, i)
    
while True:
	pass