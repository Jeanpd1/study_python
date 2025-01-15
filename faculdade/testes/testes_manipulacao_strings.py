s1 = 'Lógica de programação'        #concatenação de string vom operação e adição
s1 = s1 + ' e algoritmos'
print(s1)

 ############################

s1 = 'A' + '-' * 10 + 'B' #concatenação para repetição de caractere
print(s1)

##############################

nota = 8.5                  #composição da string com a variável
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)

nota = 8.5                  #limitando as casas decimais do resultado (.2 é o número de casas decimais após a ,)
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

##############################

jogo = "God of War"  #composição de várias váriaveis (modo antigo)
genero = "Ação"
ano = 2022

s1 =  'O jogo %s, lançado em %d, é um jogo de %s' % (jogo, ano, genero)
print(s1)

##################################

jogo = "God of War" #composição de várias váriaveis (modo novo)
genero = "Ação"
ano = 2022

s1 = "O jogo {}, lançado em {}, é um jogo de {}" .format(jogo, ano, genero)
print(s1)

###################################

s1 = 'Jean é o Deus da terra'       #Fatiamento de String
print(s1[0:5])

s1 = 'Jean é o Deus da terra'
print (s1[9:14])

s1 = 'Jean é o Deus da terra'
print (s1[:14])

##############################################

s1 = 'Sartori gosta de Carne' #descobir o tamanho da string, comando len
tamanho = len(s1)
print(tamanho)

###############################################

frase = input('Digite uma frase qualquer: ')    #Exibição da metade e exibição dos ultimos da frase
tam = len(frase) / 2
meio = frase[:int(tam)]

print(meio)

print(meio[-2:])


################################################

string = 'Jean Fabricio Rodrigues Pedersoli'  #Verificação do Comprimento da String e Impressão
comp = len(string) <= 15

print(comp)