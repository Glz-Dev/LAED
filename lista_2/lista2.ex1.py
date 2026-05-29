V=[9,42,21,14,25,3,19,33,45,6]
maior=0
segmaior=0
termaior=0
i=0
while(i<len(V)):
    if(V[i]>maior):
        termaior=segmaior
        segmaior=maior
        maior=V[i]
    elif(V[i]>segmaior and V[i]!=maior):
        termaior=segmaior
        segmaior=V[i]
    elif( V[i]>termaior and V[i]!=segmaior and V[i]!=maior):
        termaior=V[i]
    i=i+1
print("O terceiro maior elemento é:",termaior)