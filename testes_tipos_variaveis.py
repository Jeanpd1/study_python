nota = 8.5
disciplina = 'lógica de programação'    #antes do '=' é a variável e após é o valor dela
print (nota)        #imprime na tela o que está entre parênteses
print (disciplina)

print ('disciplina: ' , disciplina, '. nota:' , nota) #concatenação de variáveis com strings

#######################

a = 1
b = 5
resposta = a == b       #comparando valores de variáveis, resposta = true ou false
print(resposta)
resposta = a != b
print (resposta)

#######################

frase = 'olá, mundo!'   #imprimindo a string inteira ou apenas o endereço de cada caractere de acordo com o índice
print(frase)
print(frase[0])
print(frase[2])

################################

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