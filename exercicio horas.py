h1 = int(input("1st horario: "))
m1 = int(input("1st minutos: "))
h2 = int(input("2nd horario: "))
m2 = int(input("2nd minutos: "))

horassobrando = (m1 + m2) // 60
minutos = (m1 + m2) % 60
horas = h1 + h2 + horassobrando - 24

if horas < 0:
    horas = horas * -1
if horas > 12:
    horas = horas - 12

print(f"{horas}:{minutos}")




