'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
'''

gen = input('Digite seu gênero(m ou f):\n')


if gen.upper() == 'F':
	alt = float(input('Digite sua altura:\n'))
	conf = (62.1 * alt) - 44.7
	print(f'Seu peso ideal é {conf:.2f}')

elif gen.upper() == 'M':
	alt = float(input('Digite sua altura:\n'))
	conm = (72.7 * alt) - 58
	print(f'Seu peso ideal é {conm:.2f}')

else:
	print('Sem opcões válidas, encerrando programa...')