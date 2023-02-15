from Duration import Durarion

test = Durarion([1,20,30], [2,75,-10], [9,0,5])

test.t3 = test.t2
test.seg_total()

test.remplazar_tiempo()
test.tiempo_t1()
test.tiempo_t2()
test.tiempo_t3()