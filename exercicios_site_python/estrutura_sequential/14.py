'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
  
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.

Imprima os dados do programa com as mensagens adequadas.
'''

peso = float(input('digite o peso da pesca: '))
exce = peso - 50
multa = exce * 4

print(f'Você pescou {peso}kgs')

if peso > 50:
	print(f'Você excedeu o limite em {exce :.2f}Kgs')
	print(f'A multa ficará em R${multa}')
else:
	print('Você não pescou acima do limite')
	