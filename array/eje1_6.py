import random
media = 0
mini = 0
maxi = 0
pais = ["España", "Rusia", "Japón", "Australia"]
array_1 = [0] * 10, [0] * 10, [0] * 10, [0] * 10

for i in range(0, len(array_1)):
    for a in range(0, len(array_1[i])):
        array_1[i][a] = random.randint(140, 240)

for i in range(0, len(pais)):
    print(pais[i], array_1[i], sum(array_1[i]) / 10, min(array_1[i]), max(array_1[i]))
