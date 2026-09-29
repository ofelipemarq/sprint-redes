import socket

HOST = "httpbin.org"
PORT = 80

requisicao = (
    "GET /get?nome=felipe&curso=ciberseguranca HTTP/1.1\r\n"
    "Host: httpbin.org\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    cliente.sendall(requisicao.encode())

    resposta = b""

    while True:
        dados = cliente.recv(4096)

        if not dados:
            break

        resposta += dados

print(resposta.decode())
