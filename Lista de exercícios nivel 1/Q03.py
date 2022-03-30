# -*- coding: utf-8 -*-

#
# Calcula o juros simples
#
def juros_simples(c, i, n):
    return c * i * n


# Este é o nosso teste.
# Sabemos que 16000 * 0.04 * 4 = 2560, logo...
assert 2560 == juros_simples(16000, 0.04, 4), "juros deve ser igual a 2560"
