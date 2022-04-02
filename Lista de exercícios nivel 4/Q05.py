# -*- coding: utf-8 -*-

#
# Sua lógica...
#
def haDuplicados(lista):
    nlist = list(set(lista))
    if lista == nlist:
        return False
    else:
        return True


#
# Testes
#
assert haDuplicados([100, 200, 300, 300, 500])
assert not haDuplicados([100, 200, 300, 400, 500])
