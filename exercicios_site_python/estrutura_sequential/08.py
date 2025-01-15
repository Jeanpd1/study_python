'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

sal = float(input('Digite seu salario por hora: R$ '))
hor = int(input('Digite a quantodade de horas trabalhadas: '))

val = sal * hor

print('Você receberá R${}' .format(val))