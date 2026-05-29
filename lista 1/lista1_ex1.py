l=[9,42, 21 ,14, 28, 3, 19, 32, 46 ,6]
N=len(l)
maior=0
for i in range(N):
    if(l[i]%2!=0):
     if(l[i]>maior):
        maior=l[i]
print(maior)