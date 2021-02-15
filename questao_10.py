#10. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salary = float(input("Informe o valor do salario atual: "))
percentage = int(input("Informe a porcetagem do aumento: "))

value = salary * (percentage / 100)

print("O valor aumentado é: ", value)

new_salary = salary + value

print("Novo Salario: ", new_salary)
