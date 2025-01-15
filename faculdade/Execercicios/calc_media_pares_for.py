#calcule a média dos números pares de 1 até 100 (1 e 100 inclusos).
#Implemente o laço usando for.

x = 0
qtd = 0
for i in range(1, 101):
    if i % 2 == 0:
           x += i
           qtd += 1
media = x / qtd
print(media)

