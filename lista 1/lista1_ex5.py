#Lista não ordenada
V=[9,2,7,7,2,2,1,7,7,9]
i=0
retornar=0
N=len(V)
while(i<N):
  j=i+1
  valor=V[i]
  while(j<N):
    if(V[j]==valor*2):
      print( V[j] ,"e", valor)
      break
    j=j+1

#Lista ordenada
def selectsort(V):
  i=0
  while(i<len(V)):
    menor=i
    j=i+1
    while(j<len(V)):
      if(V[j]<V[menor]):
        menor=j
    j=j+1
    oux=V[i]
    V[i]=V[menor]
    V[menor]=oux
    i=i+1
    return V


def dobro(V):
    V=selectsort(V)
    i=0
    while(i<len(V)):
        j=i+1
        while(j<len(V)):
            if(V[j]==V[i]*2):
                print(V[j], "é o dobro de", V[i])
            j=j+1
            
        i=i+1