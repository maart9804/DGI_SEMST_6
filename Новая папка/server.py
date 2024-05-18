import socket 

server = socket.socket()

server.bind(('localhost', int(3000)))

server.listen(5)
print(server)

con, addr = server.accept()
print('connection', con)
print('connection', addr)

con.close()

server.close()