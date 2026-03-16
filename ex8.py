anoAtual = int(input('Informe o ano atual: '))
anoNasc = int(input('Informe o ano do seu nascimento: '))
idadeAnos= anoAtual - anoNasc
idadeMeses = idadeAnos * 12
idadeDias = idadeMeses * 30
idadeSemanas = idadeDias / 7
print(f'Sua idade em anos é {idadeAnos}, sua idade em meses é {idadeMeses}, sua idade em dias é {idadeDias} e sua idade semanas é {idadeSemanas:.0f}')
