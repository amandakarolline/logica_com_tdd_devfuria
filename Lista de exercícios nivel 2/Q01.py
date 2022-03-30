# -*- coding: utf-8 -*-

#
# Função que descobre se um número é par ou ímpar
#
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


#
# Testes
#
assert eh_par(8)
assert not eh_par(7)
assert eh_par(0)
