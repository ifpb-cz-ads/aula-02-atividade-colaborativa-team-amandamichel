valor = float(input('Informe o valor da mercadoria:\nR$ '))
percentual = float(input('Informe o percentual de desconto:\n'))

valorFinal = valor - valor * (percentual/100)
valorDesconto = valor - valorFinal

print('\nValor do desconto: R$ %2.f\nPreço a pagar: R$ %2.f' % (valorDesconto, valorFinal))