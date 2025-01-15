# x = 1
# while x <= 5:
#    print(x)
#   x = x + 1  # Variável de controle
# Esse incremento é importante para não haver o loop infinito
# Caso não haja, o código só imprimirá 1 infinitamente

# x = 0
# while x < 100:
#    print(x)
#    x = x + 1

##############################################################

# Modifique esse mesmo programa para exibir na tela número de 10 a 1.000.

# x = 10
# while x >= 10 and x <= 1000:
#    print(x)
#    x = x + 1

###################################################################################

# Modifique-o também para exibir na tela uma contagem regressiva do lançamento de um
# foguete, iniciando em 10 até 0 e escrevendo, após o 0, a palavra: fogo!

# x = 10
# while x > 0:
#    print(x)
#    x = x - 1
#    if x == 0:
#        print('fogo!')


#####################################################################
# Apenas valores pares dentro de um intervalo específicado.

# a = int(input('Primeiro número: '))
# b = int(input('Segundo número: '))

# while a <= b:
#    if a % 2 == 0:
#        print(a)
#    a = a + 1

##########################################################################

# Calculo de média usando variáveis acumuladoras

# soma = 0
# cont = 1
# while cont <= 5 :
#    x = float(input('Digite a {}ª nota: ' .format(cont)))
#    soma = soma + x     # 0 + o número que o usuário digitar
#    cont = cont + 1
# media = soma / 5
# print('Média final: {:.2f}' .format(media))

##########################################################################

# Validação de entrada com loop

# x = int(input('Nº maior que 0: '))

# while x <= 0:
#    x = int(input('Nº inválido, tente novamente:')) #Aparecerá enquanto a condição não for sanada

# print('Correto')

###########################################################################

# VALIDANDO DADOS DE ENTRADA COM UM LOOP

# print('Digite "sair" para encerrar')
# text = (input('Digite uma palavra para repetir:\n'))

# while text != 'sair':
#    print(text)
#    text = (input('Digite uma palavra para repetir:\n'))

# print('Saindo...')

##########################################################################

# INTERROMPENDO UM LOOP COM BREAK

# print('Digite "sair" para encerrar')

# while True:
#    text = (input('Digite uma palavra para repetir:\n'))
#    print(text)
#    if text == 'sair':
#        break
# print('Saindo...')

##############################################################

# VOLTANDO AO INÍCIO DO LOOP COM CONTINUE

# while True:
#    login = input('Login:\n')
#    if login != 'jeanpd1':
#        continue
#    senha = input('Senha:')
#    if senha == '123456':
#                break
# print('Acesso concedido')

##############################################################

# Estrutura de repetição for

# for i in range (6):
#    print(i)

# Usando a estrutura com 3 valores para contar decrescente

# for i in range (10,0,-2):      # (valor inicial, final, compaço)
#    print(i)

################################################################

# Varredura de strings com For (Fará imprimir cada uma das letras em linhas diferentes)

#x = 'Lógica de programação e algoritmos'
#for i in range(0, len(x)):      # O 'len(var)' contabiliza as caracteres
#    print(x[i])

# Varredura imprimindo na mesma linha

#x = 'Lógica de programação e algoritmos'
#for i in range(0, len(x)):
#    print(x[i], end='')


###################################################################

# Estrutura repetição aninhada com 2 while

#num = 1

#while num <= 10:
#    print('Tabuada do {}' .format(num))
#    mul = 0
#    while mul <= 10:
#       conta = num * mul
#        print('{} x {} = {} '.format(num, mul, conta))
#        mul += 1
#    num += 1

# Com 2 for

#for mul in range(1, 11):
#    print('\nTabuada do {}' .format(mul))
#    for num in range(0,11):
#        conta = num * mul
#        print('{} x {} = {}' .format(mul, num, conta))