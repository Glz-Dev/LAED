V=[7,1,9,1,7,3,9,2,1,6,8,3]

def repetidos(V,k):
    i=0
    while(i<len(V)):
        j=i+1
        while(j<len(V)):
            if(V[i]==V[j] and (j-i)<=k): #os indices se referem a menor distancia e tem que ser menor igual a K
                print("Sim")
                print(f"O número {V[i]} se repete nas posições {i} e {j}")
                return
            j=j+1
        i=i+1
    print("Não")
repetidos(V,3)