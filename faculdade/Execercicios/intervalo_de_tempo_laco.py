

#hini = int(input('Horário inicial:\n'))
#hfin = int(input('Horário final:\n'))

while True:
    hini = int(input('Horário inicial:\n'))
    hfin = int(input('Horário final:\n'))
    if hini > hfin or hini == hfin or hfin > 24:
        print('repita o processo')
    else:
        for h in range(hini, hfin + 1):

