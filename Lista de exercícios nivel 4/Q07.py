# -*- coding: utf-8 -*-

# Função que descobre a quantidade de vogais
# de uma determinada string
def contarVogais(palavra):
    vogais = 'aeiou'
    v = 0
    palavra = palavra.lower()
    for i in palavra:
        if i in vogais:
            v += 1
    return v


#
# Teste
#
palavra = "abecedario"
assert 6 == contarVogais(palavra)
assert 3 == contarVogais('Amanda')
