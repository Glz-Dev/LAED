def mediana(U, V, n):
    i = 0
    j = 0
    total = []
    while i < n and j < n:

        if U[i] < V[j]:
            total.append(U[i])
            i += 1
        else:
            total.append(V[j])
            j += 1
    while i < n:
        total.append(U[i])
        i += 1
    while j < n:
        total.append(V[j])
        j += 1
    meio1 = total[n - 1]
    meio2 = total[n]
    return (meio1 + meio2) / 2
U = list(map(int, input("Digite U: ").split()))
V = list(map(int, input("Digite V: ").split()))
n = len(U)
print("Mediana:", mediana(U, V, n))