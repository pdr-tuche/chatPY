import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost',8888))

fim= False
print('Digite cambio derligo p terminar o chat')

while not fim:
    cliente.send(input('Messagem :').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'cambio derligo':
        fim = True
    else:
        print("pessoa: {}".format(msg))
cliente.close()