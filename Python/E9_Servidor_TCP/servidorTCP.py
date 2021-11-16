# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:11:51 2021

@author: Moncho
"""

import socket
from cryptography.fernet import Fernet

TCP_IP = '127.0.0.1'
TCP_PORT = 5005 #Puedes poner otro, verifica que no lo uses ya y que sea el mismo en el cliente tcp.
BUFFER_SIZE = 2048

obj =socket.socket()
    
obj.bind((TCP_IP, TCP_PORT))
    
obj.listen()
    
conn, adress = obj.accept()
    
while True:
    data = conn.recv(BUFFER_SIZE)
    if data:
        print("Enterado. Bye!")
        break

conn.close()        
print("Conexion cerrada")        