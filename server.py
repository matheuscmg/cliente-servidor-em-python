import socket
# Cria o socket
socket_servidor = socket.socket()
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()



info = ("Você se Conectou.")
socket_cliente.send(info.encode('utf-8')) # Envia resposta
msg = socket_cliente.recv(1024)
print(msg)

res=(str("VVFFV"))
frase=str(msg)
frase=frase[2:7].upper()

acertos=0
erros=0

for i in range (0,5):

    if(res[i] == frase[i]):
      acertos = acertos+1
      print(f"Q{i+1}):Acertou ({res[i]})")
    else:
        erros = erros + 1
        (print(f"Q{i+1}):errou resposta certa era ({res[i]})"))


dif =(f'acertou {acertos} errou:{erros}  média:{(acertos/5)*10}')
socket_cliente.send(dif.encode('utf-8')) # Envia resposta
socket_cliente.send(info.encode('utf-8')) # Envia resposta
print('O usuário Digitou opções invalidas.')

