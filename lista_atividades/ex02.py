vetor= [2.5, 7.5, 10.0,4.0]
soma= 0
for i in vetor:
    soma= soma + i
media= soma/ len(vetor)
proximo= vetor[0]
if vetor[0] > media:
    menor_distancia= vetor[0] - media
else:
    menor_distancia= media - vetor[0]
for i in vetor:
    if i > media: 
        distancia= i-media
    else:
        distancia= media - i
    if distancia < menor_distancia:
        menor_distancia= distancia
        proximo= i

print("Media =",media)
print("mais proximo: ", proximo)