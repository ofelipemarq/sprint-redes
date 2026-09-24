# Exercícios — Servidor HTTP local e comunicação em rede

> Use este roteiro para registrar comandos, código, respostas e evidências da atividade.



---

## Parte 1 — Servidor HTTP local

### Entregáveis

- Arquivo criado: `index.html`
- Comando usado para iniciar o servidor na porta 8080:
  ```bash 

  ```

- Evidência de acesso a `http://localhost:8080`:

  ![Servidor HTTP local no navegador](images/servidor-local.png)

- Identificação do cliente, do servidor, do endereço IP local e da porta utilizada:

  **Resposta:**

---

## Parte 2 — Requisição HTTP manual com TCP

### Conexão TCP

- Comando usado para conectar ao servidor com `nc`:

  ```bash

  ```

### Requisição e resposta `200 OK`

- Requisição HTTP enviada:

  ```http

  ```

- Resposta HTTP recebida:

  ```http

  ```

- Evidência no terminal:

  ![Requisição e resposta 200 OK](images/http-200.png)

### Requisição e resposta `404 Not Found`

- Requisição HTTP enviada:

  ```http

  ```

- Resposta HTTP recebida:

  ```http

  ```

- Evidência no terminal:

  ![Requisição e resposta 404 Not Found](images/http-404.png)

### Questões

1. Quais diferenças você observou entre as respostas `200 OK` e `404 Not Found`?

   **Resposta:**

2. Qual é a função da linha vazia ao final dos cabeçalhos HTTP?

   **Resposta:**

---

## Parte 3 — Implementação com sockets

### Arquivos de código

- Servidor: `servidor_http.py`
- Cliente: `cliente_http.py`

### Evidências de execução do servidor

- Comando de execução:

  ```bash

  ```

- IP e porta do cliente:

  **Resposta:**

- Requisição recebida:

  ```http

  ```

- Resposta enviada:

  ```http

  ```

- Registro do encerramento da conexão:

  **Resposta:**

- Screenshot complementar do terminal:

  ![Execução do servidor com sockets](images/socket-servidor.png)

### Evidências de execução do cliente

- Comando de execução:

  ```bash

  ```

- Endereço do servidor:

  **Resposta:**

- Porta utilizada:

  **Resposta:**

- Bytes enviados:

  **Resposta:**

- Bytes recebidos:

  **Resposta:**

- Resposta exibida pelo cliente:

  ```http

  ```

- Screenshot complementar do terminal:

  ![Execução do cliente com sockets](images/socket-cliente.png)

### Extensão opcional — outro computador na rede local

- Registro da execução com o servidor em `0.0.0.0`:
- Porta não privilegiada utilizada:
- Regras de firewall verificadas:
- Cuidados adotados para não expor o serviço à Internet:

---

## Parte 4 — Cálculos de atraso e vazão

1. Um pacote possui `L = 7,5 megabits`, o enlace possui `R = 1,5 megabits por segundo` e o caminho possui `N = 2 enlaces`. Calcule o atraso aproximado sem congestionamento.

   **Resposta:**

2. Repita o exercício anterior dividindo a mensagem em três pacotes de `2,5 megabits`. Explique por que o tempo total diminui quando o roteador começa a reenviar o primeiro pacote enquanto a origem transmite o segundo.

   **Resposta:**

3. Considere um caminho com enlaces de `1 Gbps`, `100 Mbps`, `10 Mbps` e `500 Mbps`. Calcule a vazão fim a fim e identifique o gargalo.

   **Resposta:**

4. Considere um enlace de `R = 100 Mbps` e um pacote de `L = 10 megabits`. Calcule o atraso de transmissão.

   **Resposta:**

5. Considere um enlace com distância `d = 1.000 km` e velocidade de propagação `s = 2 × 10^8 m/s`. Converta as unidades e calcule o atraso de propagação.

   **Resposta:**

6. Dê um exemplo em que o atraso de transmissão seja dominante e outro em que o atraso de propagação seja dominante.

   **Resposta:**
