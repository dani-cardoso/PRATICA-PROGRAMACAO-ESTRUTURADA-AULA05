moeda1 = float(input('Quantiddade de moedas de 1 real: '))
moeda1c = float(input('Quantidade de moedas de 1 centavo: '))
moeda5 = float(input('Quantiddade de moedas de 5 centavos: '))
moeda10 = float(input('Quantiddade de moedas de 10 centavos: '))
moeda25 = float(input('Quantiddade de moedas de 25 centavos: '))
moeda50 = float(input('Quantiddade de moedas de 50 centavos: '))

total = (moeda1c * 0.01) (moeda1 * 1) + (moeda5 * 0.05) + (moeda10 * 0.10) + (moeda25 * 0.25) + (moeda50* 0.5)

print(f'O total em reais é {total:.2f}')
