'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
quanto pagou ao sindicato.
c) o salário líquido.
calcule os descontos e o salário líquido,
d) conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

sal = float(input('Quanto ganha por hora?\n'))
trab = int(input('Quantas horas foram trabalhadas?\n'))

bru = sal * trab
ir = (bru * 0.11)
inss = (bru * 0.08) 
sind = (bru * 0.05) 
liq = bru - ir - inss - sind


print(f'+ Salário Bruto : R${bru}\n- IR (11%) : R${ir:.2f}\n- INSS (8%) : R${inss:.2f}\n- Sindicato ( 5%) : R${sind:.2f}\n= Salário Liquido : R${liq}')