V=[9,2,7,7,2,2,1,7,7,9]
i=0
N=len(V)
cont=0
while(i<N):
    j=i+1
    while(j<N):
        if(V[i]>V[j] and i<j):
            cont=cont+1
        j=j+1
    i=i+1
print("A quantidade de inversões é:",cont)
