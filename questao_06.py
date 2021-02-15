#6. Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
#Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

materia1 = float(input("Informe a nota da Materia 1: "))
materia2 = float(input("Informe a nota da Materia 2: "))
materia3 = float(input("Informe a nota da Materia 3: "))

if materia1 >= 7.0 and materia2 >= 7.0 and materia3 >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado!")
