# Uma calculadora focada nos operadores usando funções condicionais

print('+ - adição\n- - subtração\n* - multiplicação\n/ - divisão\n')

a = int(input('Digite o primeiro número:\n'))
ops = input('Qual operação aplicar?\n')
b = int(input('Digite o segundo número:\n'))

if ops == '+':
    print('O resultado da soma de {} com {} é {:.2f}' .format(a , b, (a + b)))
elif ops == '-':
    print('O resultado da subtração de {} com {} é {:.2f}' .format(a , b , (a - b)))
elif ops == '*':
    print('O resultado da multiplicação de {} com {} é {:.2f}' .format(a , b , (a * b)))
elif ops == '/':
    print('O resultado da divisão de {} com {} é {:.2f}' .format(a , b , (a / b)))
else:
    print('Opção não disponível.')