# Variáveis globais

lista_livro = []  # Lista de livros
id_global = 0  # Variável global para controle do ID dos livros


# Funções

def cadastrar_livro(id):
    global id_global
    print('-' * 20, ' MENU CADASTRAR LIVRO', '-' * 20, '\n')
    print(f'ID do livro: {id_global}')
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora} # Dicionário que jogará as informações para a lista
    lista_livro.append(livro)
    print('Livro cadastrado com sucesso!')

def consultar_livro():
    print('-' * 20, ' MENU CONSULTAR LIVRO', '-' * 20, '\n')
    print('Escolha a opção desejada\n')
    print('1. Consultar Todos')
    print('2. Consultar por Id')
    print('3. Consultar por Autor')
    print('4. Retornar ao menu')
    try:
        opcao = input('>> ')
    except ValueError:
        print('Digite um número válido.')

    if opcao == '1':
        for livro in lista_livro: #Conta e printa todos os livros cadastrados
            print(livro)

    elif opcao == '2':  # Conta e compara o id inputado com o id do livro cadastrado.
        try:
            id_consulta = int(input("Digite o ID do livro: "))
        except ValueError:
            print('Digite um número válido.')
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print(livro)
                break
        else:
            print("Livro não encontrado.")

    elif opcao == '3':  # Executa a mesma coisa que o elif anterior mas comparando o autor.
        try:
            autor_consulta = input("Digite o autor do livro: ")
        except ValueError:
            print('Digite um número válido.')
        for livro in lista_livro:
            if livro['autor'] == autor_consulta:
                print(livro)

    elif opcao == '4':
        return # Retorna um valor vazio apenas para sair da função

    else:
        print("Opção inválida")


def remover_livro():
    print('-' * 20, ' MENU REMOVER LIVRO', '-' * 20, '\n')
    try:
        id_remover = int(input("Digite o ID do livro a ser removido: "))
    except ValueError:
        print('Digite um número válido.')

    for livro in lista_livro:   # Conta o id de acordo com o tamanho da lista
        if livro['id'] == id_remover:   # Compara com o id inputado para tomar a ação de remover o livro
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            return
    else:
        print("Livro não encontrado.")


# main

print('Bem vindo ao controle de livros de Jean Pedersoli')


while True:
    print('-' * 20, ' MENU PRINCIPAL', '-' * 20, '\n')
    print('Escolha a opção desejada\n')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro')
    print('3. Remover Livro')
    print('4. Encerrar Programa')
    opcao = input('>> ')

# Cada opção da estrutura condicional abaixo chama uma função diferente.
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global) # Pega a variável e joga como parâmetro "id" na função de cadastro de livros
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")
