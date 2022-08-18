# Lucas Henrique Rudiniki Costanski

arquivo = open("arquivo.txt", "r")
texto = arquivo.readlines()


vetor = []
uniao = []
inter = []
diferenca = []
cont = 0


for i in texto:
    vetor.append(i.strip())


num = int(vetor[0])


for i in range(len(vetor)):

    if (cont < num):

        #União

        if ("U" in vetor[i] and not "," in vetor[i]):
            conjuntoA = vetor[i + 1].split(', ')
            conjuntoB = vetor[i + 2].split(', ')

            for i in range(len(conjuntoA)):
                uniao.append(conjuntoA[i])

            for i in range(len(conjuntoB)):
                if (conjuntoB[i] not in uniao):
                    uniao.append(conjuntoB[i])

            a = ','.join(conjuntoA)
            b = ','.join(conjuntoB)
            aub = ','.join(uniao)
            print("União: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(a, b, aub))
            cont += 1
            uniao = []

        #Interseção

        elif ("I" in vetor[i] and not "," in vetor[i]):
            conjuntoA = vetor[i + 1].split(', ')
            conjuntoB = vetor[i + 2].split(', ')

            for i in range(len(conjuntoA)):
                for l in range(len(conjuntoB)):
                    if ((conjuntoA[i] == conjuntoB[l]) and not conjuntoA[i] in inter):
                        inter.append(conjuntoB[l])

            a = ','.join(conjuntoA)
            b = ','.join(conjuntoB)
            aib = ','.join(inter)
            print("Interseção: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(a, b, aib))
            cont += 1
            inter = []

        #Diferença

        elif ("D" in vetor[i] and not "," in vetor[i]):
            conjuntoA = vetor[i + 1].split(', ')
            conjuntoB = vetor[i + 2].split(', ')

            for i in range(len(conjuntoA)):
                if(conjuntoA[i] not in conjuntoB):
                    diferenca.append(conjuntoA[i])

            a = ','.join(conjuntoA)
            b = ','.join(conjuntoB)
            adb = ','.join(diferenca)
            print("Diferença: conjunto 1 {%s}, conjunto 2 {%s}. Resultado: {%s}" %(a, b, adb))
            cont += 1
            diferenca = []

        #Produto Cartesiano

        elif ("C" in vetor[i] and not "," in vetor[i]):
            conjuntoA = vetor[i + 1].split(', ')
            conjuntoB = vetor[i + 2].split(', ')

            a = ','.join(conjuntoA)
            b = ','.join(conjuntoB)

            print("Produto Cartesiano: conjunto 1 {%s}, conjunto 2 {%s}. Resultado:" %(a, b), end="")

            for i in range(len(conjuntoA)):
                for l in range(len(conjuntoB)):
                    print("{", conjuntoA[i], ",", conjuntoB[l],"},", end="")
                print("\n")

            cont += 1
