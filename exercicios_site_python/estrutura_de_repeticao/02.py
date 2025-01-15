'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:	
	nom = input('nome: ')
	sen = input(' senha:')
	if nom == sen:
		print(' A senha deve ser diferente do nome\n')
		continue
	else:
		print('Finalizando programa...')
		break