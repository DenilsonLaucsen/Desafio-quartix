ladoA = 25
ladoB = 25
ladoC = 30

if((ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA)):
    if(ladoA == ladoB == ladoC):
        print("Este é um triângulo equilátero")
    elif(ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
        print("Este é um triângulo isósceles")
    else:
        print("Este é um triângulo escaleno")
else:
    print("Não pode ser um triângulo")