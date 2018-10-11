#!/usr/bin/python
#jaredliu 2018.10.11 v0.1 
#from netstat -> socket topologies,
#suggest view in youdao(md) or markdown with(mermaid)
#
import socket
import os

block_ports = ['22' , '10050']
hostname = socket.gethostname()

fd = os.popen('netstat -lnt')
lines = fd.readlines()

listen_ports = []
content = lines[2:]

for line in content:
    field_port = line.split()[3].split(':')[-1]

    if field_port not in listen_ports:
        listen_ports.append(field_port)
#print listen_ports

#
#start body
fd = os.popen('netstat -nt')
lines = fd.readlines()

socket_set =[]
content = lines[2:]

for line in content:
    column_local = line.split()[3].split(':')
    column_remote = line.split()[4].split(':')
    if column_local[-1] in listen_ports:
        fx = ['passive']
    else:
        fx = ['active']
    socket_line = column_local + column_remote + fx
    socket_set.append(socket_line)
#localIP,localPort,remoteIP,remotePort,fx
#   0       1         2         3       4

socket_in = []
socket_out = []
for socket_line in socket_set:
    if socket_line[4] is 'passive' and socket_line[1] not in block_ports:
        socket_line_in = socket_line[2]+"-->|"+socket_line[1]+"x(num)|"+hostname
        socket_in.append(socket_line_in)
    elif socket_line[4] is 'active' and socket_line[3] not in block_ports:
        socket_line_out = hostname+"-->|"+socket_line[3]+"x(num)|"+socket_line[2]
        socket_out.append(socket_line_out)
    else:
        pass

#print socket_in
myset = []
myset = set(socket_in)
for line in myset:
    newline = line.replace('(num)',str(socket_in.count(line)))
    print("%s" %(newline))

#print socket_out
myset = set(socket_out)
for line in myset:
    newline = line.replace('(num)',str(socket_out.count(line)))
    print("%s" %(newline))

