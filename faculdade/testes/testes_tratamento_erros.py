# Erro de sintaxe

while True          # Faltou os dois pontos e isso calsará o erro de sintaxe
    print('Olá, mundo!')

# O erro de sintaxe ocorre quando você digita de forma errada qualquer
# parte da estutura dos comandos da linguagem.

####################################################################

# Erro de exceção

# Neste tipo de erro, a sintaxe está correta, porém, um erro durante a execução do programa
# ocorre, normalmente, devido a um dado digitado de maneira inválida e
# não tratado durante o programa

# ZeroDivisorError

100 * (2/0)     # Não existe divisão por zero

# Como tratar:

def div():  # Função criada para a tratativa do erro, geralmente todas as trativas são usadas assim
    try:    # instrução "Tentar" que vai tentar ter sucesso nos dados de entrada
        num1 = int(input('Digite um núm:'))
        num2 = int(input('Digite um núm:'))
        res = num1 / num2
# Tudo da lina 38 à 40 estiver correto, o código vai para o else (linha 46)
    except ZeroDivisionError:
        print('Não há divisão por 0')
    except:     # Sem cláusula porque qualquer erro sem ser ZeroDivision vai printar a mensagem.
        print('Algo está errado.')  # Vai aparecer por qualquer outro erro e finaliza o programa
    else:   # Esse else vai retornar o resultado da função vai printar
        return res
    finally:    # "Finalmente" sempre se executará depois de um try
        print('Executará sempre.')  # Só foi posto para ilustrar a execução do finally

print(div())

#######################################################

# ValueError

x = int(input('Digite um número: '))    #Irá ocorrer o erro caso o user coloque um string no input

# Como tratar:

while True:     # Laço de repetição para validar o dado e não cair no erro
    try:        # 'Tentativa' instrução que tenta executar a linha a seguir
        x = int(input('Digite um número: '))    # Caso o dado esteja correto e não gere uma exceção...
        break   # Cai no break e encerra o programa
    except ValueError:      # Caso a "tentativa" falhe, cai na 'Exceção' do erro 'ValueError'
        print('Digite um número válido')    # E printa essa mensagem fazendo o loop voltar




