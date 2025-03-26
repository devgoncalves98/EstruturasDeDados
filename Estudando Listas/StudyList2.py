from dataclasses import dataclass
from typing import List
import statistics

# Definição da estrutura de dados
@dataclass
class Dados:
    categoria: str
    valor: float

# Função para alimentar o array de structs
def alimentar_dados() -> List[Dados]:
    dados = [
        Dados("Categoria A", 10.0),
        Dados("Categoria B", 20.0),
        Dados("Categoria A", 15.0),
        Dados("Categoria C", 25.0),
        Dados("Categoria B", 30.0),
    ]
    return dados

# Função para gerar estatísticas dos dados tabulados
def gerar_estatisticas(dados: List[Dados]):
    # Tabular dados por categoria
    tabela = {}
    for dado in dados:
        if dado.categoria not in tabela:
            tabela[dado.categoria] = []
        tabela[dado.categoria].append(dado.valor)

    # Exibir estatísticas
    for categoria, valores in tabela.items():
        print(f"Categoria: {categoria}") #print("Categoria:  ", categoria)
        print(f"  Total de itens: {len(valores)}")
        print(f"  Soma dos valores: {sum(valores)}")
        print(f"  Média dos valores: {statistics.mean(valores):.2f}")
        print(f"  Valor máximo: {max(valores)}")
        print(f"  Valor mínimo: {min(valores)}")
        print()

# Programa principal
def main():
    # Alimentar os dados
    dados = alimentar_dados()

    # Gerar estatísticas
    gerar_estatisticas(dados)

if __name__ == "__main__":
    main()
