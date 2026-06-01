def sao_permutacoes_ordenacao(U, V):
    if len(U) != len(V):
        return False
        
    U.sort() 
    V.sort()
    for i in range(len(U)):
        if U[i] != V[i]:
            return False  
        
    return True 