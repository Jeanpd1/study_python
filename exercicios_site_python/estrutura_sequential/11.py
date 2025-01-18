'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

calca = (a * 2) * (b / 2)
calcb = (a * 3) + c
calcc = c ** 3

print(calca)
print(calcb)
print(calcc)