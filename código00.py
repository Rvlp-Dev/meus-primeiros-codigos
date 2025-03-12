nome = str(input('Digite seu nome completo: ')).strip()  #Aprendendo a usar Manipulação de textos
primeiro_nome = nome.split()[0]
print('Seu nome em maiúsculo: ', nome.upper())
print('Seu nome em minúnsculo: ', nome.lower())
print('Total de letras:', len(nome.replace(' ', '')))
print(f'Primeiro nome tem: {len(primeiro_nome)}')
idade = int(input('Digite sua idade: ')) #Aprendendo if / else
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
num = int(input('Digite um número entre 0 e 9999: ')) #Aqui dei uma perdida, mas saiu com ajuda.
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
invertido = nome[::-1]
print(f'Seu nome invertido é: {invertido}' )

#Um pouco de tudo que aprendi até agora --- 
