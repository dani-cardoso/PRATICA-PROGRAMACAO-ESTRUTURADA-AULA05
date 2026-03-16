salarioFixo = float(input('Informe o salário fixo: '))
valorVendas = float(input('Informe o valor das suas vendas: '))
comissao = valorVendas * 0.04
salarioFinal = comissao + salarioFixo 
print(f'O valor do salario mais as comissões é {salarioFinal}')
