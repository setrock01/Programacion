#ejercicio 1
import random
array_1 = [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5
array_total = [0] * 5

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i]) - 1):
        array_1[i][a] = int(input("Introduzca un numero parara la array"))

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i])):
        array_total[i] += array_1[i][a]
    array_1[i][4] = sum(array_1[i])

for i in range(0, len(array_1) - 1):
    array_total[4] += array_1[i][4] + array_total[i]
for i in range(0, len(array_1)):
    print(array_1[i])
print(array_total)
