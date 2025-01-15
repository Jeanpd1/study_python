'''def realce():
    print('|', '----' * 10, '|')
    print('|', '----' * 10, '|')

realce()
print('                   MENU')
realce()

#####################################################
# Passagem de parâmetros
def realce(s1):
    print('|', '----' * 10, '|')
    print('|', '----' * 10, '|')
    print(s1)
    print('|', '----' * 10, '|')
    print('|', '----' * 10, '|')

realce('                   MENU')


def sub2(x, y):
    res = x - y
    print(res)


sub2(7, 5)      #Muito importante manter a ordem dos valores da passagem a mesma das variáveis.

sub2(y = 7, x = 5)    #você pode forçar a ordem dos parâmetros desde que os indentifiquem na invocação

# Parâmetros opcionais

def soma3(x = 0, y = 0, z = 0):
    res =x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2)      # z foi omitido
soma3(1)              # y  e z foram omitidos
soma3()               # x, y e z foram omitidos

#######################################################################

# Escopo de variáveis

# Escopo local
def comida():     # Linha 45, 46 e 47 fazem parte de um escopo local
    ovos = 12     # Variável local da função comida
    print(ovos)   # Instrução print vai printar a variável local quando a função for invocada

comida()            #invocação da função que está no escopo global




#Escopo global
def comida():
    print(ovos)     # Vai printar a string da váriavel global

ovos = 'Estou no escopo global'  #Variável global
comida()           #invocação da função que vai printar a variável global pois elas também estão presentes nos escopos
#locais




# Ordem com que o pragram verifica as variáveis

def comida():
    ovos = 12       # Variável local
    bacon()         # Invoca a função bacon
    print(ovos)     # Printa a variável local da função comida

def bacon():
    ovos = 6        # Mesmo tendo o mesmo nome, essa váriavel local não interfere na outra variável local

comida()    #Invoca a função comida que vai printar a variável local

# Outro exemplo e sua ordem

def comida():                   # 7º função comida que foi invocada 
    ovos = 'Variável local de comida'   # 8º variável local da função comida recebe uma string
    print(ovos)                 # 9º print da variável local de comida

def bacon():                    # 3º função bacon que foi invocada
    ovos = 'Variável local de bacon'    # 4ª variável local da função bacon recebe uma string
    print(ovos)                 # 5º print da variável local de bacon
    comida()                    # 6º invoca a função comida
    print(ovos)                 # 10º print da variável local de bacon

ovos = 'Variável Global'        # 1ª variável global que recebe uma string
bacon()                         # 2º invoca a função bacon
print(ovos)                     # 11º print da variável global

# Instrução Global

# Essa instrução  faz com que você manipule as variáveis globais dentro do escopo local sem a necessidade de criar
# mais varáveis locais

def comida():
    global ovos         # indica que a variável do escopo global
    ovos = 'comida'     # altera a o valor da váriavel global de 'global' para 'comida'


ovos = 'global'         # variável global recebe a string
comida()
print(ovos)             # printa o novo valor definido na função (comida).

#############################################################################

# Retorno de valores em funções

def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res              # Com o return você pode retornar o resultado da função para o escopo global
                            #  e poder sempre usar quando quiser

retornado1 = soma3(1,2,3)   # variável que recebeu o valor da função soma3 graças ao return
print(retornado)

# forma simplificada
print(soma3(1,2,3))

# Usando o mesmo return em várias variáveis

retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print('Somatórios: {}, {} e {}' .format(retornado1, retornado2, retornado3))

#########################################################


''''''
Escreva uma função para validar uma string.
Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string
estiver entre os valores de mínimo e máximo,
e falso, caso contrário (elaborado com base
em Menezes, s. d.)
''''''

def val_str(string, min, max):
    x = input(string)
    if len(string) >= min or len(string) <= max:
        return True
    else:
        return False

res = input(val_str("Digite uma palvra entre 10 e 20 car.: ", 10, 20))

print(res)

################################################


# Função como parâmetro de função

def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)
def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

imprime_com_condicao(5, par)

#####################################################

# Função Lambda

res = lambda x: x * x       # Cria variável e atribui comando lambda, o que vem antes dos dois pontos vai ser parâmetro
                            # O que vier após os dois pontos será a conta
print(res(3))

# Atribuindo mais de um parâmetro

soma = lambda x, y: x + y        # Foram atribuídos dois parâmetros (antes dos dois pontos)
print(soma(3,5))'''
