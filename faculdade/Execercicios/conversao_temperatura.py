#Calculadora de conversão de Celsius para fahrenheits com ambas as formas de composição de variáveis

cel = float(input('Coloque uma temperatura em Celsius: '))
fah = (9 * cel/5) + 32

#Clássica
final = 'O valor dessa temperatura é de %.2f fahrenheits' %(fah)
print(final)

# Moderna
final = 'O valor dessa temperatura é de {} fahrenheits' .format(fah)
print(final)
