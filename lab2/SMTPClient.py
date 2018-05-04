# Ryan Kozak
# PLab 2a - SMTP Client

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# https://support.google.com/a/answer/176600?hl=en
mailserver = 'aspmx.l.google.com' # only sends to gmail since server doesn't support auth or TLS.
port = 25 # Non SSL/TLS for now...


# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM) # create TCP socket for server, repote port 32023
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<kozakr@ecs.csus.edu>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response.
recptTo = 'RCPT TO:<ryankozak@csus.edu>\r\n';    
clientSocket.send(recptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not recieved from server.')


# Send DATA command and print server response.
dataCmd = 'DATA\r\n'
clientSocket.send(dataCmd.encode())
recv4   = clientSocket.recv(1024).decode() 
print(recv4)
if recv4[:3] != '354':
    print('354 reply not recieved from server.')

#Send message data.
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())

# Send QUIT command and get server response.
quitCmd = 'QUIT\r\n'
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3]:
    print('221 reply not recieved from server.')
clientSocket.close();





