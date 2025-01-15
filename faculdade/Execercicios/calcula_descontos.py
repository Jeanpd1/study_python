#calculadora de descontos com ambas as formas de composição de variáveis

preco = float(input('Preço do produto: '))
discperc = float(input('Percentual de desconto: '))
valdisc = ((discperc / 100) * preco)
disc = preco - valdisc

# Clássica
res  = 'O valor do desconto será de %.1f reais \nO valor com disconto aplicado será de %.1f reais' %(valdisc, disc)
print(res)

# Moderna
res  = 'O valor do desconto será de {:.2f} reais \nO valor com disconto aplicado será de {:.2f} reais' .format(valdisc, disc)
print(res)
