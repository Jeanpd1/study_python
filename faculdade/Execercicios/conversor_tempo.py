#Conversor de tempo em segundos

dia = int(input('Informe o número de dias: '))
hor = int(input('Informe o número de horas: '))
min = int(input('Informe o número de minutos: '))
seg = int(input('informe o número de segundos: '))

res = (dia * 24 * 60 * 60) + (hor * 60 * 60) + (min * 60) + seg

print('O Total é de: {}s'.format(res))