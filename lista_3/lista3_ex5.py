def linhas_iguais(matriz, n):
    for i in range(n):
        for j in range(i + 1, n):
            iguais = True
            for k in range(n):
                if matriz[i][k] != matriz[j][k]:
                    iguais = False
                    break
            if iguais == True:
                return "Sim"
    return "Não"
matriz=[]
print(linhas_iguais(matriz, n))