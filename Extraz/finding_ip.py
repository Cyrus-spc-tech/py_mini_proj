#ijmporting nessasary module
import socket as sk

#getting hostname 
host=sk.gethostname()
print("Host Name : " + host)

#get ip address
IP=sk.gethostbyname(host)
print("IP Address : " + IP)

