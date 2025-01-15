# Receba três valores, representando os lados de um triângulofornecidos pelo usuário. Verifique se os
# Verifique se os valores formam um triângulo e classifique

a = float(input('Lado A:'))
b = float(input('Lado B:'))
c = float(input('Lado C:'))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print('Valores válidos!')
        if a == b and b == c:
            print('Equilátero')
        elif a != b and b != c and a != c:
            print('Escaleno')
        else:
            print('Isósceles')
    else:
        print('Não é triângulo')
else:
    print('Não é triângulo')