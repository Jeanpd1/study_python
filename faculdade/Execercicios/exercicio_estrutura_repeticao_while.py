#Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final. Para este intervalo
# especificado pelo usuário, calcule e mostre na tela :
#a) A quantidade de números inteiros e positivos;
#b) A quantidade de números pares;
#c) A quantidade de números ímpares;
#d) A respectiva média de cada um dos itens anteriores.
#Será necessário criar uma variável distinta para cada somatório, para cada
# quantidade e para cada média solicitada.


ini = int(input('inicio: '))
fin = int(input('final: '))

qtd_pos = 0
qtd_par = 0
qtd_im = 0

som_pos = 0
som_par = 0
som_im = 0

cont = ini

if ini < fin:
    while cont <= fin:
        if cont > 0:
            qtd_pos = qtd_pos + 1

            som_pos = som_pos + cont
        if cont % 2 == 0:
            qtd_par = qtd_par + 1
            som_par = som_par + cont
        else:
            qtd_im = qtd_im + 1
            som_im = som_im + cont
        cont = cont + 1
    med_pos = som_pos / qtd_pos
    med_par = som_par / qtd_par
    med_im = som_im / qtd_im
    print('Quantidade positivos: {}'.format(qtd_pos))
    print('Média positivos: {}'.format(med_pos))
    print('Quantidade pares: {}'.format(qtd_par))
    print('Média pares: {}'.format(med_par))
    print('Quantidade impares: {}'.format(qtd_im))
    print('Média impares'.format(med_im))

else:
    print('Valor inical <= final.')
