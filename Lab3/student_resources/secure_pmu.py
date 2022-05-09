import sys
import socket
import ssl
import random

certificate = sys.argv[1]
key = sys.argv[2]

HOST = 'localhost'
PORT = 5003

text = "This is PMU data "

cert = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
cert.load_cert_chain(certificate, keyfile=key)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = cert.wrap_socket(sock)
sock.bind((HOST, PORT))
sock.listen(1)

while True:
    sock1, addr_client = sock.accept()
    cmd = sock1.read().decode()
    if cmd == 'CMD_short:0':
        n_answer = random.randint(1, 90)
        for i in range(n_answer):
            resp = text + str(i)
            sock1.sendall(resp.encode())
    sock1.close()
    
sock.close()

while True:
	pass