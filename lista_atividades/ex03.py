lista1= [1,3,5]
lista2= [2,4,6,8,10]
lista3=[]
if len(lista1) <= len(lista2):
    menor = lista1
    maior = lista2
else:
    menor= lista2
    maior= lista1

i= 0 #posiçao 0 na lista
while i < len(menor):
    lista3.append(menor[i])
    lista3.append(maior[i])
    i= i + 1
while i < len(maior): #add os faltantes da lista 2, que tem mais elementos sobrando, o 8 e o 10
    lista3.append(maior[i])
    i=i+1
    print(lista3)