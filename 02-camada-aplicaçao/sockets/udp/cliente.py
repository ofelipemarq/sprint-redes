import socket

# IP do servidor usado no teste em duas maquinas.
# Para testar na mesma maquina, troque por "127.0.0.1".
HOST = "192.168.18.113"
PORT = 12000

frase = input("Digite uma frase: ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
    cliente.settimeout(5)
    cliente.sendto(frase.encode("utf-8"), (HOST, PORT))

    resposta, _ = cliente.recvfrom(2048)
    print("Do servidor:", resposta.decode("utf-8"))
