#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/27 18:53:11.337666
#+ Editado:	2022/01/28 18:34:07.200032
# ------------------------------------------------------------------------------
from itertools import combinations
from uteis.imprimir import jprint

import sqlite3
# ------------------------------------------------------------------------------
def espaciar(texto):
    lst_saida = []
    LST_DIVISORES = [
                '_', '-', ',', '.', ';', ':',
                '__', '--'
            ]

    for divisor in LST_DIVISORES:
        alias = texto.replace(' ', divisor)
        if alias not in lst_saida:
            lst_saida.append(alias)

    for ele in lst_saida.copy():
        for divisor in LST_DIVISORES:
            lst_saida.append(ele+divisor)
            lst_saida.append(divisor+ele)
            lst_saida.append(divisor+ele+divisor)

    return lst_saida

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    con = sqlite3.connect('alias_reservados.db')
    cur = con.cursor()
    print()

    while True:
        lst_saida = espaciar(input('Parecidos: '))

        for ele in lst_saida:
            cur.execute(f'insert into alias("valor_alias") values("{ele}")')

        print()
        con.commit()
    con.close()
    input('Intro de saída.')
# ------------------------------------------------------------------------------
