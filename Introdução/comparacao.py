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