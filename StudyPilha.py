# Classe para definir uma pilha (Stack)
class Pilha:
    def __init__(self):
        self.itens = []  # Inicializa a pilha como uma lista vazia

    # Operação Push: Adiciona elemento no topo
    def push(self, item):
        self.itens.append(item)
        print(f"Elemento {item} adicionado à pilha.")

    # Operação Pop: Remove elemento do topo
    def pop(self):
        if not self.esta_vazia():
            removido = self.itens.pop()
            print(f"Elemento {removido} removido da pilha.")
            return removido
        else:
            print("A pilha está vazia. Nenhum elemento para remover.")
            return None

    # Operação Top: Retorna o elemento no topo
    def top(self):
        if not self.esta_vazia():
            print(f"Elemento no topo: {self.itens[-1]}")
            return self.itens[-1]
        else:
            print("A pilha está vazia. Nenhum elemento no topo.")
            return None

    # Verificar se a pilha está vazia
    def esta_vazia(self):
        return len(self.itens) == 0

    # Exibir o estado atual da pilha
    def exibir(self):
        print(f"Pilha atual: {self.itens}")

# Função para ordenar a pilha como lista
def ordenar_pilha_como_lista(pilha):
    lista_ordenada = sorted(pilha.itens)  # Ordena os elementos da pilha
    print(f"Lista ordenada: {lista_ordenada}")
    return lista_ordenada

# Programa principal
def main():
    # Criando a pilha
    minha_pilha = Pilha()

    # Adicionando elementos na pilha (Push)
    minha_pilha.push(10)
    minha_pilha.push(5)
    minha_pilha.push(20)

    # Exibir o estado atual da pilha
    minha_pilha.exibir()

    # Ver elemento no topo (Top)
    minha_pilha.top()

    # Remover elemento da pilha (Pop)
    minha_pilha.pop()
    minha_pilha.exibir()

    # Ordenar elementos da pilha como uma lista
    ordenar_pilha_como_lista(minha_pilha)

# Executar o programa principal
if __name__ == "__main__":
    main()
