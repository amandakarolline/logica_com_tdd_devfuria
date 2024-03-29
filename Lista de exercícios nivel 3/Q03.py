# -*- coding: utf-8 -*-

#
# Função que calcula o MDC entre dois números
#
def mdc(num1, num2):
    m = 1
    i = 2
    while i <= num1 and i <= num2:
        while num1 % i == 0 and num2 % i == 0:
            m *= i
            num1 /= i
            num2 /= i
        i += 1
    return m

#
# Testes
#
assert 4 == mdc(24, 20)
assert 10 == mdc(30, 20)
assert 6 == mdc(18, 60)
