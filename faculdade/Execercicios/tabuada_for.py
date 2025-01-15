# tabuada digitada pelo usuário. A tabuada deve ser
# calculada até um determinado número também fornecido pelo usuário.
# Implemente o laço usando for.

tab = int(input('Qual tabuada?:\n'))
mul = int(input('Até qual multiplicado?:\n'))

for i in range(1, mul + 1):
    res = i * tab
    print('{} x {} = {}' .format(i, tab, res))
