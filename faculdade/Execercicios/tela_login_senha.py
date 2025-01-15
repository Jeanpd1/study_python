# Irá sempre pedir o login até que se cumpra a restrição

while True:
    login = input('Login:\n')
    if login != 'jeanpd1':
        continue
    senha = input('Senha:')
    if senha == '123456':
                break
print('Acesso concedido')
