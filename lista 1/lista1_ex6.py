V=[9,2,7,7,2,2,1,7,7,9]
def menorDiff(V):
    menor=abs(V[1]-V[0])
    valor1=V[0]
    valor2=V[1]
    i=0
    while(i<len(V)):
        j=i+1
        while(j<len(V)):
            diferenca=abs(V[j]-V[i])
            if(diferenca<menor):
                menor=diferenca
                valor1=V[i]
                valor2=V[j] 
            j=j+1
        i=i+1
    print("Menor diferença:", menor)
    print("Valores:", valor1, "e", valor2)

menorDiff(V)