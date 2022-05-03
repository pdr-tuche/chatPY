import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost',8888))

servidor.listen()
cliente,end = servidor.accept()

fim = False

while not fim:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'cambio derligo':
        fim = True
    else:
        print("pessoa: {}".format(msg))
        cliente.send(input('Mensagem: ').encode('utf-8'))
cliente.close()
servidor.close()