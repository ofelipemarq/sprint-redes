import socket

HOST = "127.0.0.1"
PORT = 8080

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando ao servidor {HOST}:{PORT}...")

cliente.connect((HOST, PORT))

requisicao = (
    "GET / HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)

dados_enviados = requisicao.encode()

cliente.sendall(dados_enviados)

print(f"Bytes enviados: {len(dados_enviados)}")

resposta = cliente.recv(4096)

print(f"Bytes recebidos: {len(resposta)}")
print("\nResposta do servidor:")
print(resposta.decode())

cliente.close()

print("\nConexão encerrada.")