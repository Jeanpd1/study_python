# Calculadora de IMC usando Condicionais.

peso = float(input('Coloque seu peso (Kg): '))
altura = float(input('Coloque sua altura (M): '))

imc = float(peso / altura ** 2)

if(imc >= 25):
    print('Seu IMC está auterado, busque um médico!')
else:
    print('Você está saudável!')
