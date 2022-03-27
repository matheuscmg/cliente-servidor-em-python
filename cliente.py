import socket
host = socket.gethostname()
porta = 9999

# Cria o socket
s = socket.socket()
try:
# Tenta se conectar ao servidor
    s.connect((host, porta))
except Exception as erro:
    print(str(erro))


print('Conexão efetuada com',host)
#Recebe informações disponiveis
msg = s.recv(1024)
print(msg.decode('utf-8'))

#Aguarda usuario digitar opção para monitorar
menu = input('Digite o seu gabarito:')
s.send(menu.encode('utf-8')) #Envia opção escolhida pelo usuario
#recebe informações
info = s.recv(1024)
print(info.decode())