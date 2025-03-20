import datetime
ano = int(input('Ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamente e seu alistamento será em {ano_atual + (18 - idade)}')
elif idade == 18:
    print('Você precisa ir se alistar')
elif idade > 18:
    print(f'Você deveria ter se alistado em {ano_atual - (idade - 18)}')