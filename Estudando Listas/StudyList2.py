from dataclasses



#função para gerar estatísticas dos dados tabulados
def gerar_estatisticas(dados: List[Dados]):
    #Tabular dados por categoria
    tabela = {}
    for dado in dados:
        if dado.categoria not in tabela:
            tabela[dado.categoria] = []
        tabela[dado.categoria].append(dado.valor)
    #Exibir estatisticas
    for categoria,valores in tabela.items()
        print(f"Categoria: {categoria}")
        print(f"    Total de itens: {len(valores)}")
        print(f"    Soma dos Valores: {sum(valores)}")
        print(f"    Média dos valores: {statistics.mean(valores):.2f}")
        print(f"    Valor Maximo: {max(valores)}")
        print(f"    Valor Minimo: {min(valores)}")
        print()