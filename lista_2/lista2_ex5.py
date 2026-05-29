V=[7,1,9,1,7,3,9,2,1,6,8,3]
def aparecer(V,k):
 i=0
 cont=0
 while(i<len(V)):
  cont=0
  j=0
  while(j<len(V)):
   if(V[i]==V[j]):
    cont=cont+1
   j=j+1
 if(cont==k):
  print(f"O numero {V[i]} aparece {k} vezes")
  return
 else:
  print("não")
 
        
aparecer(V,3) 