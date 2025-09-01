def AlgoritmosAvaros(pesos, valores, capacidad):
    objetos=[]
    for i in range(len(pesos)):
        relacion = valores[i]/pesos[i]
        objetos.append([relacion, pesos[i],valores[i]])

    objetos.sort(reverse=True)
    valor_total =0
    fracciones =[]

    for relacion, peso, valor in objetos:
        if capacidad ==0:
            break
        if peso<=capacidad:
            valor_total+= valor
            fracciones.append(1)
            capacidad-= peso
        else:
            fracciones.append(capacidad/peso)
            valor_total +=valor*(capacidad/peso)
            capacidad = 0
    return valor_total

pesos1 = [10,20, 30, 40, 50]
valores1 = [60, 100,120, 140,150]
capacidad1 = 100

pesos2 = [2, 5, 10,3, 8]
valores2 = [20, 30, 50, 40,45]
capacidad2 = 15

pesos3 = [8, 3, 5, 2, 4, 9,1]
valores3 = [16, 9, 20,6, 10,24, 5]
capacidad3 = 20

resultado1 = AlgoritmosAvaros(pesos1, valores1, capacidad1)
resultado2 = AlgoritmosAvaros(pesos2, valores2, capacidad2)
resultado3 = AlgoritmosAvaros(pesos3, valores3, capacidad3)

print(f"Resultado conjunto 1: {resultado1}")
print(f"Resultado conjunto 2: {resultado2}")
print(f"Resultado conjunto 3: {resultado3}")