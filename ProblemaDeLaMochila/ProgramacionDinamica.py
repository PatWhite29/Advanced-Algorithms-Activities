def ProgramacionDinamica(peso, valor, CapacidadMax):
    mejorValor = [0]*(CapacidadMax+1)
    for i in range(len(peso)):
        p = peso[i]
        v = valor[i]
        for capacidadActual in range(CapacidadMax, p - 1, -1):
            if mejorValor[capacidadActual- p]+v > mejorValor[capacidadActual]:
                mejorValor[capacidadActual]=mejorValor[capacidadActual - p]+v
    return mejorValor[CapacidadMax]

peso = [4, 5, 2, 8, 1]
valor = [12, 9, 3, 16, 2]  
CapacidadMax = 10

resultado =ProgramacionDinamica(peso, valor, CapacidadMax)
print(f"Valor maximo de la mochila: {resultado}")