'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

f = float(input('Digite a temperatura em fahrenheit\n'))

conv = 5 * ((f - 32)  / 9)

print('{} fahrenheit equivalem a {} celsuus' .format(f, conv))