#uso do array
"""arrayCompras= ['banana','laranja','maçã']
for i in arrayCompras:
    print(i)"""

#uso e importação do numpy
"""import numpy as np

arrayNumeros = np.array([5,6,7,4,2,5])
tam=len(arrayNumeros)
for x in range(tam):
    print(arrayNumeros[x])"""

#1 exercicio com array (criar um array de tamanho 5 e preencher com o nome de 5 alunos
"""arrayAlunos = [" "]*5
tam=len (arrayAlunos)
for i in range(tam):
    arrayAlunos [i] = input("aluno: ")
print(arrayAlunos)"""

"""arrayAlunos = [" "]*3
tam=len (arrayAlunos)
for i in range(tam):
    arrayAlunos[i] = input("aluno: ")
for w in range(tam):
    print(w, arrayAlunos[w])"""


#2 exercicio de array
#part 1: ler 5 notas#part 2: calcular a media geral#parte 3: quantas notas ficaram a cima da media geral
"""arrayNotas=[" "]*5
tam=len(arrayNotas)
soma = 0
cont = 0
for y in range(tam):
    arrayNotas[y] = float(input("nota: "))
for x in range(tam):
    soma = soma + arrayNotas[x]
media = soma/tam
for h in range(tam):
    if arrayNotas[h]>media:
        cont=cont+1

print(f"media da turma é {media}, e {cont} alunos ficram acima da media")"""


arrayNumeros = [0]*10
arrayNumfim = [0]*10
tam=len(arrayNumeros)
for i in range(tam):
    arrayNumeros [i] = int(input("numero: "))
mult = int(input("multiplicador: "))

for x in range(tam):
    arrayNumfim[x]=arrayNumeros[x]*mult
print(arrayNumeros)
print(mult)
print(arrayNumfim)
































