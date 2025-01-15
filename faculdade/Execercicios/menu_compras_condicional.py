#Escolher uma dentre as opções e calcular o preço

selecao = int(input('Escolha uma fruta! \n  1. Maçã\n  2. Laranja\n  3. Banana\n   '))
quant = int(input('Qual é a quantidade?\n   '))

if(selecao == 1):
    valtotal1 = float(2.30 * quant)
    print('Sua(s)', quant, 'maçã(s) ficou(aram) em R${}.'.format(valtotal1))
else:
    if(selecao == 2):
        valtotal2 = float(3.60 * quant)
        print('Sua(s)', quant, 'laranja(s) ficou(aram) em R${}.'.format(valtotal2))
    else:
        if (selecao == 3):
            valtotal3 = float(1.85 * quant)
            print('Sua(s)', quant, 'banana(s) ficou(aram) em R${}.'.format(valtotal3))
        else:
            print('Esta opção não está disponível.')