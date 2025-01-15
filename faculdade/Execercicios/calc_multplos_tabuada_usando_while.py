# retorna a tabuada completa do multiplo escolhido pelo usuario

con = 1
mul = int(input('Qual taboada?   '))



while con <= 10:
	conta = con * mul
	print('{} x {} =' .format(con, mul) , conta)
	con = con + 1
