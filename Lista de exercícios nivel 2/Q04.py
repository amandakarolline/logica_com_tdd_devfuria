# -*- coding: utf-8 -*-

#
# Converte fahrenheit em celsius
#
def toCelsius(fahrenheit):
    c = (fahrenheit - 32) * 5 / 9
    return c


#
# Converte celsius em fahrenheit
#
def toFahrenheit(celsius):
    f = 32 + 9 * celsius / 5
    return f


#
# Testes
#
celsius = 100
fahrenheit = 212

assert celsius == toCelsius(fahrenheit)
assert fahrenheit == toFahrenheit(celsius)
