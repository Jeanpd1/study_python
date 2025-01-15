#Calculadora para média de notas

nome = input('Nome do Aluno: ')
nota1 = float(input('nota do 1º bimestre: '))
nota2 = float(input('nota do 2º bimestre: '))
nota3 = float(input('nota do 3º bimestre: '))
nota4 = float(input('nota do 4º bimestre: '))

medianota = (nota1+nota2+nota3+nota4)/4
mediapas = 7
mediafin = medianota >= mediapas        #true = passou de ano ; false = reprovou

print('A sua média do ano foi: ' , medianota)

print(mediafin)
