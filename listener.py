#!/usr/bin/env python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.15", 4444))
listener.listen(0)
print("[+] Waiting for connection.\n")
listener.accept()
print("\n[+] Got a connection.\n")