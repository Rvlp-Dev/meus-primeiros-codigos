import random
mao = str(input('Pedra, papel ou tesoura? ')).lower()
pedra = str('pedra')
papel = str('papel')
tesoura = str('tesoura')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
if mao == pedra and pc == papel or mao == papel and pc == tesoura or mao == tesoura and pc == pedra:
    print(f'Você perdeu! TENTE NOVAMENTE ... Eu escolhi {pc}')
elif mao == pedra and pc == tesoura or mao == papel and pc == pedra or mao == tesoura and pc == papel:
    print(f'Você ganhou de mim! PARABENS ... Eu escolhi {pc}')
else:
    print(f'Empate, vamos tentar novamente, pois eu escolhi {pc}')