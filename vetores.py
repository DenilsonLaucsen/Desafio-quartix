"""Construir um gerenciador de vetor. Escreva um programa que contenha as seguintes 3 funções:
search(v, x): Caso o elemento x esteja no vetor v, retorna o índice correspondente à primeira ocorrência do elemento x no vetor v. Caso contrário, retornará -1.
insert(vetor, valor, indice): Insere o elemento x na posição de índice k do vetor v. Caso k for superior ou igual ao comprimento do vetor v, preencher as posições até o índice k com o valor 0.
remove(v, x): Remove a primeira ocorrência do valor x no vetor v. Retorna -1, caso não haja nenhuma ocorrência.
Escreva uma função principal para executar as seguintes instruções:
"""
def search(vetor, valor):
    count = 0
    for x in vetor:
        if(x == valor):
            return count
        count += 1
    return -1

def insert(vetor, valor, indice):
    if(indice > len(vetor)):
        for x in range(len(vetor)):
            vetor[x] = 0
    else:
        vetor[indice] = valor
    print(vetor)
            
def remove(vetor, valor):
    count = 0
    for x in vetor:
        if(x == valor):
            vetor.pop(count)
            print(vetor)
            return 1
        count += 1
    return -1

"""
v = [0, -1, -2, -2, -4, -5]
rs = search(v, -4)
print("search -2: " + str(rs))

rs = search(v, 2)
print("search 2: " + str(rs))

len(v)

#insert(v, 50, 5)
#insert(v, 10, 10)
"""
v = [0, -1, -2, -2, -4, -5]
rr = remove(v, -4)
print(rr)


