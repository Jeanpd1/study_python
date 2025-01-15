print('Bem vindo a loja do Jean ru:4680338')

valun = float(input('Entre com o valor unitário do produto: R$'))   # Valor unitário
qtd = int(input('Entre com a quantidade do produto: '))             # Quantidade do produto

valt = valun * qtd      # Variável que vai armazenar o valor total da compra

if valt < 2500:
    print('O valor sem desconto foi {}' .format(valt))
    print('Valor de compra mínimo para desconto não atingido')
elif valt >= 2500 and valt < 6000:
    desc4 = valt * 0.04     # Variável que descobre o valor da porcentagem de desconto
    desc42 = valt - desc4   # Váriável que aplica o desconto
    # As variáveis acima iram se repetir por toda a estrutura condicional com seus respectivos valores
    print('O valor sem desconto foi R${}'.format(valt))
    print('O valor com desconto foi R${} (desconto de 4%)'.format(desc42))
elif valt >= 6000 and valt < 10000:
    desc7 = valt * 0.07
    desc72 = valt - desc7
    print('O valor sem desconto foi R${}'.format(valt))
    print('O valor com desconto foi R${} (desconto de 7%)'.format(desc72))
else:
    desc11 = valt * 0.11
    desc112 = valt - desc11
    print('O valor sem desconto foi R${}'.format(valt))
    print('O valor com desconto foi R${} (desconto de 11%)'.format(desc112))

