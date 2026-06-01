def existe_repetido(matriz, n):
    for i in range(n):
        for j in range(n):
            atual = matriz[i][j]
            for x in range(n):
                for y in range(n):
                    if i == x and j == y:
                        continue
                    if matriz[x][y] == atual:
                        return "Sim"
    return "Não"
matriz=[]
print(existe_repetido(matriz, n))