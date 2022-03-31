# -*- coding: utf-8 -*-

#
# Seu código
#
def somarLista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


#
# Seu teste
#
lista = [10, 20, 30, 0]
assert 60 == somarLista(lista)
