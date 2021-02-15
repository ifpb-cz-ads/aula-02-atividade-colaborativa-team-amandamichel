#14. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
#alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input("Informe a quantidade de KM percorrido: "))
days = float(input("Informe a quantidade de dias do aluguel: "))

result = (days * 60) + (km * 0.15)

print (result)
