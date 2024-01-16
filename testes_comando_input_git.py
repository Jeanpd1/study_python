idade = input('Qual sua idade?')  # comando input simples
print(idade)

#############################

nome = input('Qual seu nome?')  # comando input com composição de váriaveis
print('Olá {}, Seja bem-vindo!'.format(nome))

#####################################

nota = float(input('Qual nota você recebeu na disciplina?'))  # conversão de dados de entrada
print('Você tirou nota {}'.format(nota))

#######################################

num1 = int(input('Digite o primeiro número'))  # exercício 1 proposto
num2 = int(input('Digite o segundo número'))

print('O resultado da sua soma é: ', (num1 + num2))


###########################################

dia = int(input('Informe o número de dias: '))  # exercício 2 proposto
hor = int(input('Informe o número de horas: '))
min = int(input('Informe o número de minutos: '))
seg = int(input('informe o número de segundos: '))

res = (dia * 24 * 60 * 60) + (hor * 60 * 60) + (min * 60) + seg

print('O Total é de: {}s'.format(res))


#####################################################################################

preco = float(input('Preço do produto: '))          #exercício 3 proposto
discperc = float(input('Percentual de desconto: '))
valdisc = ((discperc / 100) * preco)
disc = preco - valdisc

# Clássica
res  = 'O valor do desconto será de %.1f reais \nO valor com disconto aplicado será de %.1f reais' %(valdisc, disc)
print(res)

# Moderna
res  = 'O valor do desconto será de {:.2f} reais \nO valor com disconto aplicado será de {:.2f} reais' .format(valdisc, disc)
print(res)


###########################################################################################

cel = float(input('Coloque uma temperatura em Celsius: '))      #exercício 4 proposto
fah = (9 * cel/5) + 32

#Clássica
final = 'O valor dessa temperatura é de %.2f fahrenheits' %(fah)
print(final)

# Moderna
final = 'O valor dessa temperatura é de {} fahrenheits' .format(fah)
# print(final)

