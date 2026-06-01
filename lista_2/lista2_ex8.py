def repetidos_proximos_bruta(V, k):
    n = len(V)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if V[i] == V[j]:
                return True
                
    return False