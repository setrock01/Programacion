from point import Dado


dado=Dado(20,7)

print(dado.caras)
print(dado)
print(dado.roll)

print(dado.caras)
print(dado)

print(dado.roll)

dados=[Dado(9,7),Dado(20,8),Dado(8,8),Dado(),Dado(50)]


for i in range(len(dados)):
    print(f"Tirando dado {i+1}")
    print(dados[i].roll)

