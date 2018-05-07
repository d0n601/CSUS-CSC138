# Ryan Kozak
# PLab 2a - SMTP Client

import ssl
import base64
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with mailserver
mailserver = "smtp.gmail.com" # Gmail
port = 587 # STARTLS

# Create socket called clientSocket and establish a TCP connection with mailserver
initialSocket = socket(AF_INET, SOCK_STREAM) # create TCP socket for server
initialSocket.connect((mailserver, port))


recv = initialSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCmd= 'HELO Alice\r\n'
initialSocket.send(heloCmd.encode())
recv_helo = initialSocket.recv(1024).decode()
print(recv_helo)
if recv_helo[:3] != '250':
    print('250 reply not received from server.')


# Request an encrypted connection
startTlsCommand = 'STARTTLS\r\n'
initialSocket.send(startTlsCommand.encode())
tls_recv = initialSocket.recv(1024).decode()
print(tls_recv)
if tls_recv[:3] != '220':
    print ('220 reply not received from server')

# Wrap the socket into an encrypted socket
clientSocket = ssl.wrap_socket(initialSocket, ssl_version=ssl.PROTOCOL_SSLv23)

# Send the AUTH LOGIN command and print server response.
authCmd = 'AUTH LOGIN\r\n'
clientSocket.write(authCmd.encode())
recv_auth = clientSocket.read(1024).decode()
print (recv_auth)
if recv_auth[:3] != '334':
    print ('334 reply not received from server')

# Send username and print server response.
username = base64.b64encode(b'csc138man@gmail.com')
username = username.decode()+'\r\n'
clientSocket.write(username.encode())
recv_user = clientSocket.read(1024).decode()
print (recv_user)
if recv_user[:3] != '334':
    print ('334 reply not received from server')

# Send password and print server response.
password = base64.b64encode(b'PASSWORDGOESHERE')
password = password.decode()+'\r\n'
clientSocket.write(password.encode())
recv_pword = clientSocket.read(1024).decode()
print (recv_pword)
if recv_pword[:3] != '235':
    print ('235 reply not received from server')

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<csc138man@gmail.com>\r\n'
clientSocket.send(mailFrom.encode())
recv_from = clientSocket.recv(1024).decode()
print(recv_from)
if recv_from[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
recptTo = 'RCPT TO:<ryankozak@csus.edu>\r\n';    
clientSocket.send(recptTo.encode())
recv_to = clientSocket.recv(1024).decode()
print(recv_to)
if recv_to[:3] != '250':
    print('250 reply not recieved from server.')

# Send DATA command and print server response.
dataCmd = 'DATA\r\n'
clientSocket.send(dataCmd.encode())
recv_data   = clientSocket.recv(1024).decode()
print(recv_data)
if recv_data[:3] != '354':
    print('354 reply not recieved from server.')

#Send message data.
clientSocket.send(msg.encode())
# End message period.
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.read(1024).decode()
print(recv_msg)
if recv_msg[:3] != '250':
    print ('250 reply not received from server.')

# Send QUIT command and get server response.
quitCmd = 'QUIT\r\n'
clientSocket.send(quitCmd.encode())
recv_quit = clientSocket.recv(1024).decode()
print (recv_quit)
if recv_quit[:3] != '221':
    print ('221 reply not received from server.')

clientSocket.close()

