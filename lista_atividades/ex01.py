import random
vetor = []
contagem= [0,0,0,0,0,0]
i=0
while i < 100:
    numero=random.randint(1,6)
    vetor.append(numero)
    if numero == 1:
        contagem[0]= contagem [0] + 1
    if numero == 2:
        contagem[1]= contagem[1]+ 1
    if numero== 3:
        contagem[2]= contagem[2] + 1
    if numero== 4:
        contagem[3]= contagem[3] + 1
    if numero== 5:
        contagem[4]= contagem[4]+ 1
    if numero == 6:
        contagem[5]= contagem[5] +1
        i=i+1
print("lancamentos:")
print(vetor)
print()
print ("contagem:")
print(contagem)