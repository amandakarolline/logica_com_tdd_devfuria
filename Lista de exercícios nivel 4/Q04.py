# -*- coding: utf-8 -*-

lista = [6, 10, 4, 21, 9]
iMaior = 0
iMenor = 0

#
# Sua lógica
#
for i in range(len(lista)):
    if lista[i] > lista[iMaior]:
        iMaior = i
    if lista[i] < lista[iMenor]:
        iMenor = i

#
# Testes
#
assert iMaior == 3
assert iMenor == 2
