# -*- coding: utf-8 -*-

def somarDigitos(numero):
    palavra = str(numero)
    soma = 0
    for i in palavra:
        soma += int(i)
    return soma


assert 8 == somarDigitos(2015), "a soma dos dígitos de 2015 devem ser 8"
assert 15 == somarDigitos(456), "a soma dos dígitos de 456 devem ser 15"
