from Duration_profe import  Duration

t1 = Duration(20,80,70)

print ("t1:" , t1)

t2= Duration (1,2,100)
print("t2: " , t2)

print ("suma : " , t1 + t2)

print ("resta: ", t2 - t1)

t1.add_sub_time(segundos_add=-25)
print(t1)

t3=Duration(2,75,-10)

print(t3)

t4=Duration(3,-1,-60)
print(t4)
