peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / altura ** 2
print(f'seu Imc é {imc:.2f}')
if imc < 18.5:
	print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
	print('Peso normal')
elif imc >= 25 and imc <= 29.9:
	print('Sobrepeso')
else:
	print('Obesidade')