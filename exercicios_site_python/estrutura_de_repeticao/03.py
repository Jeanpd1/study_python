'''
Faça um programa que leia e valide as seguintes informações:
a) Nome: maior que 3 caracteres;
b) Idade: entre 0 e 150;
c)Salário: maior que zero;
d) Sexo: 'f' ou 'm';
e) Estado Civil: 's', 'c', 'v', 'd';
'''
while True:
	nom = input('Digite seu nome: ')

	if len(nom) < 3:
		print('Nome deve ter mais que 3 letras\n')
		continue
		
	age = int(input('Digite sua idade: '))
	
	while age < 0 or age > 150:
		age = int(input('Digite uma idade válida: '))
		
	sal = float(input('Digite o salário: '))
	
	while sal < 0:
		age = int(input('Digite um valor maior que zero: '))
		
	sex = input('Digite o sexo: ')
	
	while sex != 'f' and 'm':
		age = input('Digite uma opção válida: ')
	