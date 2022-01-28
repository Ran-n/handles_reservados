#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/28 17:03:49.763291
#+ Editado:	2022/01/28 18:04:59.419154
# ------------------------------------------------------------------------------
from itertools import combinations, combinations_with_replacement
from uteis.imprimir import jprint
# ------------------------------------------------------------------------------
def parecidos(texto):
    lst_saida = []

    texto = texto.lower()
    lst_texto = texto.split(' ')
    lst_texto_capi = [ele.capitalize() for ele in lst_texto]
    lst_texto_total = [*lst_texto, *lst_texto_capi]
    print(lst_texto_total)

    lst_combis = []
    for n in range(1, int(len(lst_texto_total)/2)+1):
        lst_combis += list(combinations_with_replacement(lst_texto_total, n))

    return lst_texto, lst_combis

def proba(lst, lst_texto):
    for ele in lst[::-1]:
        if len(ele) == 0:
            if ele in lst:
                lst.remove(ele)
        elif len(ele) > 1:
            for ele1, ele2 in zip(ele, lst_texto):
                if ele1.lower() != ele2.lower():
                    if ele in lst:
                        lst.remove(ele)
    return lst

# ------------------------------------------------------------------------------
lst_texto, lst_combis = parecidos('anxo Ledo arias')
print(lst_texto)
print(lst_combis)
print(len(lst_combis))
print()
jprint(proba(lst_combis, lst_texto))
print(len(proba(lst_combis, lst_texto)))

# ------------------------------------------------------------------------------
