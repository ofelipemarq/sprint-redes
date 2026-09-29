import socket

# Para receber conexoes de outras maquinas da rede local.
# Para um teste apenas em loopback, pode ser usado "127.0.0.1".
HOST = "0.0.0.0"
PORT = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen(1)

    print(f"Servidor TCP ouvindo em {HOST}:{PORT}...")

    while True:
        conexao, endereco = servidor.accept()

        with conexao:
            print(f"Conexao de: {endereco}")

            dados = conexao.recv(1024)
            if not dados:
                continue

            frase = dados.decode("utf-8")
            print(f"Recebido: {frase}")

            resposta = frase.upper()
            conexao.sendall(resposta.encode("utf-8"))
