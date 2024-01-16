#Calculadora para informar o valor de locações de carros

km = float(input('Quantos kilometros foram percorridos? '))
d = int(input('Quantos dias de locação? '))
precokmr = 0.15
precod = 60

vfinal = (km * precokmr) + (d * precod)
print('O valor total da locação é de R${:.2f}'. format(vfinal))