# calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:

kwh = float(input('Quantos kWh consumidos: '))
ins = input('Qual o tipo de instalação?\n R - Residência\n I - Industria\n C - comércio\n')

if ins == 'r':
    if kwh <= 500:
        preco = kwh * 0.40
        print('Residendical\n O valor ficará em R${:.2f}'.format(preco))
    else:
        kwh > 500
        preco = kwh * 0.65
        print('Residendical\n O valor ficará em R${:.2f}'.format(preco))

elif ins == 'i':
    if kwh <= 5000:
        preco = kwh * 0.55
        print('Industrial\n O valor ficará em R${:.2f}'.format(preco))
    else:
        kwh > 5000
        preco = kwh * 0.60
        print('Industrial\n O valor ficará em R${:.2f}'.format(preco))

elif ins == 'c':
    if kwh <= 1000:
        preco = kwh * 0.55
        print('Comercial\n O valor ficará em R${:.2f}'.format(preco))
    else:
        kwh > 1000
        preco = kwh * 0.60
        print('Comercial\n O valor ficará em R${:.2f}S'.format(preco))
else:
    print('Opção inválida')
