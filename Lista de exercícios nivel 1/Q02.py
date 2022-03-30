# -*- coding: utf-8 -*-

#
# Retorna o custo final da fabricação de um carro
#
def custoFinal(custo_fabrica):
    custo_distribuidor = 0.28 * custo_fabrica
    custo_imposto = 0.45 * custo_fabrica

    return custo_fabrica + custo_distribuidor + custo_imposto


#
# Teste
#
assert 17300 == custoFinal(10000), "'custoFinal' deve ser igual a 17300"
