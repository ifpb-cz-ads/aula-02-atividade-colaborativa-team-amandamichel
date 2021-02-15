# 12. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.


km = float(input("Informe a quantidade de quilometros: "))
vel_media = float(input("Informe a velocidade media: "))

temp_viagem = (km / vel_media) * 3600

horas = temp_viagem // 3600
minutos = (temp_viagem % 3600) / 60
segundos = temp_viagem % 60

print("O tempo da viagem eh: ", horas, "hora(s) " , minutos, "minuto(s) ", segundos,"segundo(s)")
