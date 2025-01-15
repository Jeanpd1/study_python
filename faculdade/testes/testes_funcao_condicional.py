#Condicional simples com números inteiros.

#x = int(input('Digite o primeiro valor:'))
#y = int(input('Digite o segundo valor:'))

#if(x > y):
#    print('O primeiro valor digitado é maior que o segundo')

###############################################################

#Condicional composta, indentificar números impares ou pares.

#x = int(input('Coloque um número:'))

#if(x % 2 == 0):
#    print('O número é par!')
#else:
#    print('O número é impar!')

##################################################################

# Expressões lógicas e algebra booleana

#x = True
#y = False

#print(not x)    # not == inverte(nega) resultado
#print(not y)

#x = True
#y = False
#print(x and y)  #and == ambas as entradas devem ser true(1) para saída ser true

#x = True
#y = False
#print(x or y)   #or == basta uma entrada ser true(1) para saída ser true

######################################################################################

#Expressões lógicas/booleanas

#x = 10
#y =  1

#res = not x > y     #Seguindo regra de precedência, resolve primeiro o relacional(>) e depois o lógico(not)
#print(res)


#x = 10
#y = 1
#z = 5.5

#res = x > y and z == y
#print(res)


#O aluno deve tirar média 7 em todas as matérias para ser aprovado

#a = float(input('Nota matéria 1: '))
#b = float(input('Nota matéria 2: '))
#c = float(input('Nota matéria 3: '))

#res = (a >= 7) and (b >= 7) and (c >= 7)

#if(res == True):
    #print("Aprovado")
#else:
    #print('Reprovado')

#####################################################

#Condicional aninhada

#selecao = int(input('Escolha uma fruta! \n  1. Maçã\n  2. Laranja\n  3. Banana\n   '))
#quant = int(input('Qual é a quantidade?\n   '))

#if(selecao == 1):
#    valtotal1 = float(2.30 * quant)
#    print('Sua(s)', quant, 'maçã(s) ficou(aram) em R${}.'.format(valtotal1))
#else:
#    if(selecao == 2):
#        valtotal2 = float(3.60 * quant)
#        print('Sua(s)', quant, 'laranja(s) ficou(aram) em R${}.'.format(valtotal2))
#    else:
#        if (selecao == 3):
#            valtotal3 = float(1.85 * quant)
#            print('Sua(s)', quant, 'banana(s) ficou(aram) em R${}.'.format(valtotal3))
#        else:
#            print('Esta opção não está disponível.')

#Em python o aninhamento é importante pois a linguagem interpreta os espaçamentos.

##########################################################################################

