# -*- coding: utf-8 -*-

# Função que descobre se um número é positivo ou negativo
#
# retornará 1 caso positivo
# retornará 0 caso negativo
#
def eh_positivo(numero):
    if numero >= 0:
        return 1
    else:
        return 0


#
# Seus testes
#
assert eh_positivo(100) == 1
assert eh_positivo(0) == 1
assert eh_positivo(-100) == 0
