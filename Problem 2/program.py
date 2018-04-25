from itertools import permutations
input = open("submitInput.txt","r")
output = open("submitOutput.txt","w")
lineas = input.readlines()
T = int(lineas[0])
for x in range(1,T+1): #para cada caso
    S = lineas[x]
    base = len(S)-1 #base de la codificación (nº de letras)

    mayor = []
    for i in range(base-1,-1,-1):
        mayor.insert(len(mayor),i) #Números en orden descendente

    menor = []
    menor.insert(0,1)       #Un 1 en la posición 0
    for i in range(0,base): #Números en orden ascendente sin el 1
        if i != 1:
            menor.insert(len(menor),i)

    codMayor = 0
    for i in range (len(mayor)-1,-1,-1):
        codMayor = codMayor + (mayor[i] * (base**(base-i-1)))

    codMenor = 0
    for i in range (len(menor)-1,-1,-1):
        codMenor = codMenor + (menor[i] * (base**(base-i-1)))

    output.write("Case #{}: {}\n".format(x,(codMayor-codMenor)))
