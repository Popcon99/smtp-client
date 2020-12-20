import socket
import smtplib

ClientSocket = socket.socket()
host = '192.168.78.7'
port= 2525
print('Waiting for connection')
try:
   ClientSocket.connect((host, port))
   smtplib.SMTP('mail.your-domain.com', 2525)
except socket.error as e:
   print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:

   Input =  input('From:')
   Input = input('To: ')
   Input = input('message:')
   input.close()
   ClientSocket.send(str.encode(Input))
   Response = ClientSocket.recv(1024)
ClientSocket.close()

