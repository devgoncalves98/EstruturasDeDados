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