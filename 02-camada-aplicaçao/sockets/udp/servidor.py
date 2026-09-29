import socket

# Para receber datagramas de outras maquinas da rede local.
# Para um teste apenas em loopback, pode ser usado "127.0.0.1".
HOST = "0.0.0.0"
PORT = 12000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
    servidor.bind((HOST, PORT))

    print(f"Servidor UDP ouvindo em {HOST}:{PORT}...")

    while True:
        dados, origem = servidor.recvfrom(2048)

        frase = dados.decode("utf-8")
        print(f"Recebido de {origem}: {frase}")

        resposta = frase.upper()
        servidor.sendto(resposta.encode("utf-8"), origem)
