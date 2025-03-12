#Código mais complicado de entender pra mim, principalmente a lógica por trás e a linguagem de != 0 significar que não é dividido.
ano = int(input('Digite o ano: ')) 
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Esse é um ano bissexto')
else:
    print('Não é um ano bissexto')
