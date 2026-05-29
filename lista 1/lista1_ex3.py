V=[9,42,21,14,25,3,19,33,45]
k=40
def maiorK(V,k):
    distancia=abs(V[1]-k)
    i=0
    valor=0
    while(i<len(V)):
        distancia=abs(V[i]-k)
        if(distancia>maior):
            maior=distancia
            valor=V[i]
        i=i+1
    return valor
