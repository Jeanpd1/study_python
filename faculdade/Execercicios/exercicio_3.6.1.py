# Acumula os valores digitados pelo user e faz a média.


num_dig = 0 	# acumulador
qtd_num = 0	 #contador
while True: 	#truthy
	x = int(input('Digite um número:\n'))
	if x > 0:
		num_dig += x
		qtd_num += 1
		continue
	if not x :	 #falsey
		break
		
media = num_dig / qtd_num
print('A somatória deu {} e a quantidade de entradas foi {}, a  média será {}' .format(num_dig, qtd_num, media))