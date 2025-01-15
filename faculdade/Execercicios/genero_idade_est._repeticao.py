# Pergunte idade e gênero até que o user coloque um valor negativo na idade

while True:
    age = int(input('Sua idade: '))
    if age < 0:
        print('Encerrando...')
        break
    gen = input('Gênero: ')
    if gen == 'm' or gen == 'M':
        print('Boa noite senhor, sua idade é {}\n' .format(age))
    else:
        if gen == 'f' or gen == 'F':
            print('Boa noite senhora, sua idade é {}\n' .format(age))
        else:
            print('Genêro inexistente')

