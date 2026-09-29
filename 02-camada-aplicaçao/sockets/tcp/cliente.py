import socket

# IP do servidor usado no teste em duas maquinas.
# Para testar na mesma maquina, troque por "127.0.0.1".
HOST = "192.168.18.113"
PORT = 12000

frase = input("Digite uma frase: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.settimeout(5)
    cliente.connect((HOST, PORT))
    cliente.sendall(frase.encode("utf-8"))

    resposta = cliente.recv(1024)
    print("Do servidor:", resposta.decode("utf-8"))
