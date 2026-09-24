import socket

HOST = "127.0.0.1"
PORT = 8080

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))

servidor.listen(1)

print(f"Servidor aguardando conexão em {HOST}:{PORT}")

conexao, endereco_cliente = servidor.accept()

print(f"Cliente conectado: {endereco_cliente}")

requisicao = conexao.recv(1024)

print("Requisição recebida:")
print(requisicao.decode())

resposta = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain; charset=utf-8\r\n"
    "Content-Length: 18\r\n"
    "\r\n"
    "Ola do servidor!\n"
)

conexao.sendall(resposta.encode())

print("Resposta enviada.")

conexao.close()
servidor.close()

print("Conexão encerrada.")