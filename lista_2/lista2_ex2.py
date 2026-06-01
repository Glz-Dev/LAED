def kesimo_maior(L, k):
    L.sort() 
    return L[len(L) - k]   # o umtimo elemnto e n-1 o pesultimo e n-2 entao o k-eximo e L[len(n)-k]


L = [7, 1, 9, 3, 6, 8]
k = int(input("Digite k: "))
print("K-ésimo maior:", kesimo_maior(L, k))