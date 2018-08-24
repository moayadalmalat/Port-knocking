from scapy.all import *
from itertools import permutations
from time import sleep
import socket
def SendPkt(ip,port):
    ip=IP(src="127.0.0.1",dst=ip) #IP Attacker
    SYN=TCP(sport=64349,dport=port,flags="S",seq=12345)
    send(ip/SYN)

def TestPort(ip,port):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((ip,port))
	return result 

ports = [22,666,8890] # Ports Victim
#for ports in permutations(ports):
#	print(ports)
#	print(TestPort('10.0.0.9', 31337)) #Vicim ip,port
for port in ports:
	SendPkt('10.0.0.9',port) # IP Victim




		