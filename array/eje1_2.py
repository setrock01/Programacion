import random
import time
limite = 40


def barraprogreso(segmento, total, longitud):
    porcentaje = segmento / total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{'#' * completado}{'^' * restante}{porcentaje:.2%}]"
    return barra


array_1 = [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5
array_total = [0] * 5

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i]) - 1):
        array_1[i][a] = random.randint(100, 999)

for i in range(0, len(array_1)):
    print(array_1[i])
print(array_total)

for i in range(limite + 1):
    time.sleep(0.05)
    print(barraprogreso(i, limite, 40), end="\r")

print("\n")

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i])):
        array_total[i] += array_1[i][a]
    array_1[i][4] = sum(array_1[i])

for i in range(0, len(array_1) - 1):
    array_total[4] += array_1[i][4] + array_total[i]
for i in range(0, len(array_1)):
    print(array_1[i])
print(array_total)
