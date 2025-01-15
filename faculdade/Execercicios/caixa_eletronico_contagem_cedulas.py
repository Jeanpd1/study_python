# Imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Apenasvalores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$5 e R$1

saq = int(input('Valor do saque (R$):\n'))

while True:
    if saq >= 100:
        ced100 = saq // 100
        saq -= ced100 * 100
        print('Qtd. notas de 100: {}' .format(ced100))
        if not saq:
            break
    if saq >= 50:
        ced50 = saq // 50
        saq -= ced50 * 50
        print('Qtd. notas de 50: {}' .format(ced50))
        if not saq:
            break
    if saq >= 20:
        ced20 = saq // 20
        saq -= ced20 * 20
        print('Qtd. notas de 20: {}' .format(ced20))
        if not saq:
            break
    if saq >= 10:
        ced10 = saq // 10
        saq -= ced10 * 10
        print('Qtd. notas de 100: {}' .format(ced10))
        if not saq:
            break
    if saq >= 5:
        ced5 = saq // 5
        saq -= ced5 * 5
        print('Qtd. notas de 5: {}' .format(ced5))
        if not saq:
            break
    if saq:
        ced1 = saq // 1
        print('Qtd. notas de 1: {}'.format(ced1))
        break