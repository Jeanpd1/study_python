# Exercício para descobrir se o usuário tem idade o suficiente para tirar CNH
# usando comandos condicionais

nome = input('Digite seu nome: ')
anonasc = int(input('Digite seu ano de nascimento: '))
anoatua = int(input('Digite o ano atual: '))
idade = anoatua - anonasc

print('\nSua idade é {} anos.'.format(idade))

if idade >= 18:
    print('Você já é maior de idade e pode tirar sua CNH!')
else:
    print('Você ainda não atingiu a idade necessária para a CNH')
