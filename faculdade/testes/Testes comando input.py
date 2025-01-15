idade = input('Qual sua idade?')  # comando input simples
print(idade)

#############################

nome = input('Qual seu nome?')  # comando input com composição de váriaveis
print('Olá {}, Seja bem-vindo!'.format(nome))

#####################################

nota = float(input('Qual nota você recebeu na disciplina?'))  # conversão de dados de entrada
print('Você tirou nota {}'.format(nota))

#######################################

num1 = int(input('Digite o primeiro número'))  # exercício 1 proposto pelo professor
num2 = int(input('Digite o segundo número'))

print('O resultado da sua soma é: ', (num1 + num2))

########################################

x = int(input('Digite o número inteiro: '))  # solução do exercício 1 professor
y = int(input('Digite outro número inteiro: '))

res = 'O resultado da soma de %i com %i é %i.' % (x, y, x + y)  # maneira Clássica
print(res)

res = 'O resultado da soma de {} com {} é {}.'.format(x, y, x + y)  # maneira atual
print(res)

###########################################

dia = int(input('Informe o número de dias: '))  # exercício 2 proposto pelo professor
hor = int(input('Informe o número de horas: '))
min = int(input('Informe o número de minutos: '))
seg = int(input('informe o número de segundos: '))

res = (dia * 24 * 60 * 60) + (hor * 60 * 60) + (min * 60) + seg

print('O Total é de: {}s'.format(res))

#################################################################

d = int(input('Quantos dias? '))  # solução do exercício 2 professor
h = int(input('Quantos horas: '))
m = int(input('Quantos minutos? '))
s = int(input('Quantos segundos? '))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)

# Maneira clássica
res = 'O total de segundos calculados é %i.' % total
print(res)

# Maneira moderna
res = 'O total de segundos calculados é {}'.format(total)
print(res)

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

#########################################################################################

preco = float(input('Digite o preço do produto: '))     #solução do exercício 3 professor
p = float(input('Digite o percentual de desconto (0-100%): '))
desconto = preco * (p / 100)
final = preco - desconto

#clássica
print('O preço do produto é %.2f. Desconto de %.0f%%.' % (preco, p))
print('Valor calculado de desconto: %.2f. Valor final do produto: %.2f' % (desconto, final))

# Moderna
print('O preço do produto é {}. Desconto de {}%.' .format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}' .format(desconto, final))

###########################################################################################

cel = float(input('Coloque uma temperatura em Celsius: '))      #exercício 4 proposto
fah = (9 * cel/5) + 32

#Clássica
final = 'O valor dessa temperatura é de %.2f fahrenheits' %(fah)
print(final)

# Moderna
# final = 'O valor dessa temperatura é de {} fahrenheits' .format(fah)
# print(final)

############################################################################

# c = float(input('Digite uma temperatura em Celsius: '))    #solução do exercício 4 professor
# f = (9 * c / 5) + 32

# clássica
#
# Moderna
# print('Celsius: {}. Fahrenheit: {}' .format (c,f))
