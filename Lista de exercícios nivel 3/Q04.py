# -*- coding: utf-8 -*-

#
# Função mmc
#
def mmc(num1, num2):
    a, b = num1, num2
    d = 1
    i = 2
    while i <= a and i <= b:
        while a % i == 0 and b % i == 0:
            d *= i
            a /= i
            b /= i
        i += 1
    m = num1 * num2 / d
    return m


#
# Teste
#
# 2 * 2 * 3 * 5 = 60
assert 60 == mmc(12, 20)
