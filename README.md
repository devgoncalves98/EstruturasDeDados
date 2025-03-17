### EstruturasDeDados

# Introdução
## README.md
**O que são Estruturas de Dados?**
Estruturas de dados são formas organizadas de armazenar e manipular informações para torná-las eficientes. São essenciais na ciência da computação, pois impactam diretamente a performance dos algoritmos.

**Exemplos do mundo real:**
- Um sistema bancário que precisa gerenciar transações.
- Um GPS que calcula a melhor rota.
- Uma rede social que armazena e exibe conexões de amigos.

# Definição-Importância
## README.md
**Estruturas de dados lineares vs. não lineares**
- Lineares: listas, filas e pilhas.
- Não lineares: árvores e grafos.

Impacto no desempenho: um código bem estruturado pode reduzir o tempo de processamento e consumo de memória.

## comparacao.py
```python
import time

# Sem estrutura de dados adequada
dados = []
for i in range(1000000):
    dados.append(i)
    
start = time.time()
dados.index(999999)  # Busca ineficiente
end = time.time()
print(f"Tempo sem estrutura eficiente: {end - start:.5f}s")

# Com estrutura de dados otimizada (conjunto)
dados_set = set(dados)
start = time.time()
999999 in dados_set  # Busca eficiente
end = time.time()
print(f"Tempo com estrutura eficiente: {end - start:.5f}s")
```

# Conceitos-Fundamentais
## Alocação-Estática
### README.md
A alocação estática ocorre em tempo de compilação. A memória é definida antes da execução.

### exemplo_estatica.py
```python
arr = [0] * 5  # Lista de tamanho fixo
print(arr)
```

## Alocação-Dinâmica
### README.md
A alocação dinâmica ocorre em tempo de execução. A memória pode ser ajustada conforme necessário.

### exemplo_dinamica.py
```python
arr = []
for i in range(5):
    arr.append(i)  # Expansão dinâmica
print(arr)
```

# Estruturas-Lineares
## Listas
### README.md
Lista é uma estrutura ordenada onde cada elemento tem um índice.

### lista.py
```python
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]
```

## Filas
### README.md
Fila segue o princípio FIFO (First In, First Out).

### fila.py
```python
from collections import deque
fila = deque()
fila.append(1)
fila.append(2)
print(fila.popleft())  # Remove o primeiro (1)
```

## Pilhas
### README.md
Pilha segue o princípio LIFO (Last In, First Out).

### pilha.py
```python
pilha = []
pilha.append(1)
pilha.append(2)
print(pilha.pop())  # Remove o último (2)
```

# Aplicação Prática
## README.md
**Problema:** Gerenciar pedidos em um restaurante (fila de atendimento).

### aplicacao.py
```python
from collections import deque
fila_pedidos = deque()

def adicionar_pedido(pedido):
    fila_pedidos.append(pedido)
    print(f"Pedido {pedido} adicionado.")

def atender_pedido():
    if fila_pedidos:
        pedido = fila_pedidos.popleft()
        print(f"Pedido {pedido} atendido.")
    else:
        print("Nenhum pedido na fila.")

adicionar_pedido("Pizza")
adicionar_pedido("Hambúrguer")
atender_pedido()
atender_pedido()
```

---

Isso cobre todas as instruções da atividade! Agora é só subir para o GitHub. 🚀
