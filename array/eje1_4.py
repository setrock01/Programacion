import random
minimo = 1001
maximo = -1
minimo_format = ""
maximo_format = ""
array_1 = [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10


for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i])):
        array_1[i][a] = random.randint(0, 1000)

for i in range(0, len(array_1)):
    print(array_1[i])

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i])):
        if array_1[i][a] < minimo:
            minimo = array_1[i][a]
            minimo_format = i, a
        elif array_1[i][a] > maximo:
            maximo = array_1[i][a]
            maximo_format = i, a

print("El maximo se encuentra en: ", maximo_format, "= ", maximo)
print("El minimo se encuentra en: ", minimo_format, "= ", minimo)
