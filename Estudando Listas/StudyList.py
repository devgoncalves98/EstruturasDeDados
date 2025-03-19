#Teste 1
#Nesse teste estudo as listas e suas aplicações com numeros

# Criando uma lista
numeros = [10, 20, 30, 40]

# Inserindo um elemento
numeros.append(50)  # Adiciona o número 50 no final

# Removendo um elemento
numeros.remove(20)  # Remove o número 20

# Acessando um elemento pelo índice
print(numeros[1])  # Exibe o segundo elemento

# Testando a ordenação de lista
print(numeros)

# Inserindo um elemento
numeros.append(15) # Adciona o numero 15 ao final
numeros.append(25) # Adciona o numero 25 ao final
numeros.append(35) # Adciona o numero 35 ao final

print(numeros)
# Ordenando a lista
numeros.sort()  

print(numeros)  # Saída: [10, 30, 40, 50]



##Teste 2
# Neste teste estudo as listas e suas aplicações com nomes e uma forma diferente de remover termos de acordo com o indice

#Criação da lista com nomes
pessoas = ['pedro', 'paulo' , 'abdiel', 'marcos', 'jonas']

#Exibição da lista como esta no momento
print(pessoas)

#Adição de um nome nome -> henrique 
pessoas.append('henrique')

#Exibição da lista como esta no momento
print(pessoas)

#Ordenação da lista
pessoas.sort()

#Exibição da lista como esta no momento
print(pessoas)

#Remoção de um nome de acordo com o indice 
del pessoas[3]

#Exibição da lista como esta no momento
print(pessoas)

#Outra maneira de fazer isso e armazenar os nomes removidos é:
removidos = pessoas.pop(3)

#Exibição da lista como esta no momento
print(pessoas)
#Exbição de uma lista com os nomes removidos em pop
print(removidos)