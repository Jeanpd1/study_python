# Funcionários com mais de 5 anos de empresa ganharam 20% de bônus sobre o salário
# O restante ganhará 10%

sal = float(input('Digite seu salário (R$): '))
entrada = int(input('Digite seu ano de entrada: '))
atual = int(input('Digite o ano atual: '))

bon20 = sal * (20/100)
bon10 = sal * (10/100)


tempo = atual - entrada
print('Você está na empresa a {} anos' .format(tempo))


if tempo >= 5:
    print('Sua bonificação será de R${}' .format(bon20))
else:
    print('Sua bonificação será de R${}'. format(bon10))
