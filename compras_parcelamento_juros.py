# Calculadora que acrescenta juros à forma de pagamento desejada

a = float(input('Digite o valor total da compra:\n R$'))
b = input('Qual será a forma de pagameno?\n 1. À vista\n 2. 3 parcelas sem juros\n 3. 5 parcelas\n 4. 10 parcelas\n')

if b == '1':
    vist = a - (a * 0.05)
    print('Valor total: R${:.2f}  (5% desc.)'.format(vist))

elif b == '2':
    parc3 = a / 3
    print('Parcelas: 3x de R${:.2f}\nValor total: R${:.2f}  (sem juros)'.format(parc3, a))

elif b == '3':
    parc5 = ((a + (a * 0.02)) / 5)
    total5 = (a + (a * 0.02))
    print('Parcelas: 5x de R${:.2f}\nValor total: R${:.2f}  (2% juros a.m.)'.format(parc5, total5))

elif b == '4':
    parc10 = ((a + (a * 0.08)) / 10)
    total10 = (a + (a * 0.08))
    print('Parcelas: 10x de R${:.2f}\nValor total: R${:.2f}  (8% juros a.m.)'.format(parc10, total10))
