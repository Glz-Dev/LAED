V=[5,3,1,10,2,13,9,12,4,7]
soma=0
i=0
while(i<len(V)):
 soma=soma+V[i]
 i=i+1
media=soma/len(V)
menor=abs(media-V[0])
maisprox=0
valor=V[0]
while(i<len(V)):
 menor=(media-V[i])
 if(menor>maisprox):
   maisprox=menor
   valor=V[i]
 i=i+1
print("A média é:",media)
print("O valor mais proximo da média é:",valor)