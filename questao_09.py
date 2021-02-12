dias = float(input('Informe a quantidade de dias:\n'))
horas = float(input('Informe a quantidade de horas:\n'))
minutos = float(input('Informe a quantidade de minutos:\n'))
segundos = float(input('Informe a quantidade de segundos:\n'))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print('\n%.1f dia(s), %.1f hora(s), %.1f minuto(s) e %.1f segundos tem um total de %.1f segundo(s).' % (dias,horas,minutos,segundos,total))