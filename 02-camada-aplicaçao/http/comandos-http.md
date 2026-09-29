# Comandos utilizados — prática HTTP

## GET com query string

```bash
curl -i "https://httpbin.org/get?nome=felipe&curso=ciberseguranca"
```

## POST com JSON

```bash
curl -i -X POST "https://httpbin.org/post" \
  -H "Content-Type: application/json" \
  -d '{"nome":"felipe","curso":"ciberseguranca"}'
```

## Header customizado

```bash
curl -i "https://httpbin.org/headers" \
  -H "X-Lab-Redes: camada-aplicacao"
```

## HTTP manual sobre TCP

```bash
nc httpbin.org 80
```

Depois, dentro da conexão:

```http
GET /get?nome=felipe&curso=ciberseguranca HTTP/1.1
Host: httpbin.org
Connection: close

```

A linha em branco após os cabeçalhos encerra a seção de cabeçalhos.

## Cliente HTTP em Python

```bash
python3 cliente_http.py
```
