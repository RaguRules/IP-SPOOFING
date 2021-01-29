
import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread
import struct


print(" __       __            __                                                      __                      _______                                __                                                                           ")
print("|  \  _  |  \          |  \                                                    |  \                    |       \                              |  \                                                                          ")
print("| $$ / \ | $$  ______  | $$  _______   ______   ______ ____    ______         _| $$_     ______        | $$$$$$$\  ______    ______   __    __| $$_______         _______   ______    ______  __     __   ______    ______  ")
print("| $$/  $\| $$ /      \ | $$ /       \ /      \ |      \    \  /      \       |   $$ \   /      \       | $$__| $$ |      \  /      \ |  \  |  \\$/       \       /       \ /      \  /      \|  \   /  \ /      \  /      \ ")
print("| $$  $$$\ $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\       \$$$$$$  |  $$$$$$\      | $$    $$  \$$$$$$\|  $$$$$$\| $$  | $$ |  $$$$$$$      |  $$$$$$$|  $$$$$$\|  $$$$$$\\$$\ /  $$|  $$$$$$\|  $$$$$$\ ")
print("| $$ $$\$$\$$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$        | $$ __ | $$  | $$      | $$$$$$$\ /      $$| $$  | $$| $$  | $$  \$$    \        \$$    \ | $$    $$| $$   \$$ \$$\  $$ | $$    $$| $$   \$$")
print("| $$$$  \$$$$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$        | $$|  \| $$__/ $$      | $$  | $$|  $$$$$$$| $$__| $$| $$__/ $$  _\$$$$$$\       _\$$$$$$\| $$$$$$$$| $$        \$$ $$  | $$$$$$$$| $$      ")
print("| $$$    \$$$ \$$     \| $$ \$$     \ \$$    $$| $$ | $$ | $$ \$$     \         \$$  $$ \$$    $$      | $$  | $$ \$$    $$ \$$    $$ \$$    $$ |       $$      |       $$ \$$     \| $$         \$$$    \$$     \| $$      ")
print("\$$      \$$  \$$$$$$$ \$$  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$          \$$$$   \$$$$$$        \$$   \$$  \$$$$$$$ _\$$$$$$$  \$$$$$$   \$$$$$$$        \$$$$$$$   \$$$$$$$ \$$          \$      \$$$$$$$ \$$      ")
print("                                                                                                                           |  \__| $$                                                                                       ")
print("                                                                                                                            \$$    $$                                                                                       ")
print("                                                                                                                             \$$$$$$                                                                                        ")

print("\n")

print("Waiting to be connected with a client....")

HOST = ''
PORT = 6633

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

data = s.recvfrom(100000)
packet = data[0]
address = data[1]
header = struct.unpack("!BBHHHBBHBBBBBBBB", packet[:20])

if (header[6] == 6):
    protocol = "TCP"
elif (header[6] == 17):
    protocol = "UDP"
else:
	print("Something otherthan TCP or UDP protocol is received.")

print("\nProtocol: ", protocol + " (Via RAW SOCKET)")
print("Address: ", address)
print("Header: ", header)
print("\nWhole data: {}\n".format(data))
print()
s.close()
