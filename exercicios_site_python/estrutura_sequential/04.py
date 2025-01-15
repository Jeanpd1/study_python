'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

print('Digite as notas de cada bimestre.\n')

not1 = float(input('nota 1° bimestre: '))
not2 = float(input('nota 2° bimestre: '))
not3 = float(input('nota 3° bimestre: '))
not4 = float(input('nota 4° bimestre: '))

media = (not1 + not2 + not3 + not4) / 4

print(' sua media final foi {}' .format(media))