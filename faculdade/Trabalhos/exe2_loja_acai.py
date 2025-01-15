
print('Bem-vindo a loja de Gelados do Jean Pedersoli')
print('------------------Cardápio-------------------')
print('---| Tamanho | Cupuaçu (CP) | Açai (AC) |----')
print('---|    P    |   R$ 9, 00   |  R$ 11,00 |----')
print('---|    M    |   R$ 14, 00  |  R$ 16,00 |----')
print('---|    G    |   R$ 18, 00  |  R$ 20,00 |----')
print('---------------------------------------------')

preco = 0
while True:
    sab = input('Entre com o sabor desejado (CP/AC): ')
    while sab != 'CP' and sab != 'cp' and sab != 'AC' and sab != 'ac':  # Laço de repetição que verifica o sabor
        print('Sabor inválido, tente novamente.\n')
        sab = input('Entre com o sabor desejado (CP/AC): ')


    tam = input('Entre com o tamanho desejado (P/M/G): ')   # Laço de repetição que verifica o tamanho
    while tam != 'P' and tam != 'p' and tam != 'M' and tam != 'm' and tam != 'G' and tam != 'g':
        print('Tamanho inválido, tente novamente.\n')
        tam = input('Entre com o tamanho desejado (P/M/G): ')

    # Ambos os loops acima só se quebram se o input estiver de acordo com o cardápio

# A estrutura condicional abaixo vai selecionar o item a ser printado e somado ao valor de acordo com a combinação
# que o usuário inputar nas variaveis sab e tam
    if (sab == 'cp' or sab == 'CP') and (tam == 'p' or tam == 'P'):
        print('Você pediu CUPUAÇU no tamanho P: R$9,00\n')
        preco += 9
    elif (sab == 'cp' or sab == 'CP') and (tam == 'm' or tam == 'M'):
        print('Você pediu CUPUAÇU no tamanho M: R$14,00\n')
        preco += 14
    elif (sab == 'cp' or sab == 'CP') and (tam == 'g' or tam == 'G'):
        print('Você pediu CUPUAÇU no tamanho G: R$18,00\n')
        preco += 18
    elif (sab == 'ac' or sab == 'AC') and (tam == 'p' or tam == 'P'):
        print('Você pediu AÇAÍ no tamanho P: R$11,00\n')
        preco += 11
    elif (sab == 'ac' or sab == 'AC') and (tam == 'm' or tam == 'M'):
        print('Você pediu AÇAÍ no tamanho M: R$16,00\n')
        preco += 16
    elif (sab == 'ac' or sab == 'AC') and (tam == 'g' or tam == 'G'):
        print('Você pediu AÇAÍ no tamanho G: R$20,00\n')
        preco += 20

    add = input('Deseja pedir mais alguma coisa?')
    while add !=  's' and add != 'S' and add != 'n' and add != 'N': # Laço que verifica a resposta da pergunta
        add = input('Digite uma resposta válida: ')

    # A condicional abaixo vai determinar se o programa volta pro começo do loop ou se encerra o programa printando
    # o valor total do pedido
    if add == 's' or add == 'S':
        continue
    elif add == 'n' or add == 'N':
        print('Pedido finalizado.')
        break
print(f'O valor total a ser pago é R${preco}')