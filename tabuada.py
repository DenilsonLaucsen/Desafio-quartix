#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.
numTabuada = 5

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Tabuada do " + str(numTabuada))
for x in tabuada:
    print(numTabuada * x)