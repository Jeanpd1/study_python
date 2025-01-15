# As funções seguem uma estrutura parecida com tratamentos de excessão, loops e estruturas condicionais.

# Funções

def escolha_servico():
    print('Escolha o tipo de serviço desejado:')
    print('DIG - Digitalização')
    print('ICO - Impressão colorida')
    print('IBO - Impressão preto e branco')
    print('FOT - Fotocópia')
    while True:
        serv = input('>> ')
        if serv.upper() == 'DIG':  # Define o retorno dependendo do input do usuário
            return 1.10
        elif serv.upper() == 'ICO':
            return 1
        elif serv.upper() == 'IBO':
            return 0.40
        elif serv.upper() == 'FOT':
            return 0.20
        else:
            print('Escolha inválida\nEntre com o tipo de serviço desejado novamente.')
            continue


def num_pagina():
    global x  # Invoquei a várivel para a estrutura condicional atribuir um valor a ela
    while True:  # e assim fazer o calculo de paginas na fstring.
        pags = 0
        try:     # Trata qualquer excessão antes de cair na estrutura condicional
            pags = int(input('\nEntre com o número de páginas: '))
        except ValueError:
            print('Digite um número válido.')
            continue
        if pags < 20:
            x = 1  # É preciso atribuir 1 para a divisão de páginas não ser feita por 0 caso não haja desconto
            return pags  # Não há desconto
        elif pags >= 20 and pags < 200:
            x = 0.85
            return pags * 0.85  # Desconto de 15%
        elif pags >= 200 and pags < 2000:
            x = 0.80
            return pags * 0.80  # Desconto de 20%
        elif pags >= 2000 and pags < 20000:
            x = 0.75
            return pags * 0.75  # Desconto de 25%
        else:
            print(('\nNão aceitamos tantas páginas de uma vez.\nPor favor entre com o número de páginas novamente.'))
            continue


def servico_extra():
    print('\nDeseja adicionar mais algum serviço?')
    print('1 - Encardenação Simples - R$15')
    print('2 - Encardenação Capa dura - R$40')
    print('0 - Não desejo mais nada.')
    while True:
        try:
            add = int(input('>> '))
        except ValueError:
            print('Digite um número válido.')
            continue
        if add == 1:
            return 15
        elif add == 2:
            return 40
        elif add == 0:
            return 0
        else:
            print('Digite uma opção válida.')
            continue


# Main
print('Bem vindo a copiadora de Jean Pedersoli\n')

x = 0  # Essa variável foi criada para deixar o nº de páginas inteiro, pois a função num_pag() retorna o valor ja com o disconto aplicado.

servico = escolha_servico()  # Essas variáveis servem para armazenar o valor das funções para serem manipuladas pela fórmula da variável "total"
numpags = num_pagina()  # Também foram utilizadas para serem invocadas na fstring
extra = servico_extra()

total = float(servico) * float(numpags) + float(extra)  # Converte os dados monetários para float para cálculo de valores.


print(f'Total: R${total:.2f} (Serviço: R${servico:.2f} * Páginas: {int(numpags / x)} + extra R${extra:.2f})')

'''
Na linha 93 na fstring eu faço a operação inversa do desconto com o nº de páginas 
para a saída ficar com o número exato que o usuário colocou
'''