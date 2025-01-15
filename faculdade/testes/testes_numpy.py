
# É possível criar uma lista usando o for mas gera muito custo para o computador.


num_elementos = 100000000
lista_elementos = []
for x in range(num_elementos):
    lista_elementos.append(x)
    print(lista_elementos[-1])


# Utilizando o numpy, usa-se bem menos memória


import numpy as np  #invoca o numpy
num_elementos = 100000000
array_elementos = np.arange(num_elementos)  #usa a função arange (parecisa com o for)
print(array_elementos[-1])


# Criando array(listas) com métodos


import numpy as np
print(f'Criação de array numpy usando o método .array: \n {np.array([0,1,2,3,4,5])}\n')
# cria alista com todos os elementos
print(f'Criação de array numpy usando o método .ones: \n {np.ones([15])}\n')
# cria uma lista com nº1, entre colchetes eu defino quantas vezes o 1 aparecerá
print(f'Criação de array numpy usando o método .zeros: \n {np.zeros([10])}\n')
# mesma coisa que o .ones mas com zeros
print(f'Criação de array numpy usando o método .arange: \n {np.arange([100])}\n')
# criará uma lista com o número de elementos determinado
print(f'Criação de array numpy usando o método .linspace: \n {np.linspace([0, 40, 41])}')
#cria uma lista  dentro do intervalo específicado e com o núm de elementos setado.


# Criando números randômicos


import numpy as np
rng = np.random.default_rng()
print(rng.random(10))


# Vetor, matriz e tensor


import numpy as np
rng = np.random.default_rng()
vetor = rng.random(4)
print(f'Array com 1 dimensão (VETOR) randômico:\n{vetor}\n')
matriz = rng.random(4,4)
print(f'Array com 2 dimensões (MATRIZ) randômico:\n{matriz}\n')
tensor = rng.random(4,4,4)
print(f'Array com 3 ou mais dimensões (TENSOR) randômico:\n{tensor}\n')


