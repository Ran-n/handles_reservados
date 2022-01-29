#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/27 18:53:11.337666
#+ Editado:	2022/01/29 01:01:58.818574
# ------------------------------------------------------------------------------
from itertools import permutations
import sqlite3
from typing import List, Tuple
from unidecode import unidecode

from uteis.ficheiro import cargarJson
# ------------------------------------------------------------------------------
def espaciar(texto: str) -> List[str]:
    """
    Dado un string devolvecho con eses divisores e sen espazos
    """
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
def pop(lista, indice):
    lista.pop(indice)
    return lista

def parecidos(texto: str) -> List[Tuple[str]]:
    lst_saida = []
    texto = texto.lower()

    lst_texto = texto.split(' ')
    lst_texto_capi = [ele.capitalize() for ele in lst_texto]
    lst_texto_up = texto.upper().split(' ')

    lst_texto_total = [*lst_texto, *lst_texto_capi, *lst_texto_up]

    for n in range(1, len(lst_texto)+1):
        lst_saida += list(permutations(lst_texto_total, n))

    for tupla in lst_saida[::-1]:
        for index, ele in enumerate(tupla):
            if ele.lower() in [elto.lower() for elto in pop(list(tupla).copy(), index)]:
                lst_saida.remove(tupla)
                break


    return lst_saida, lst_texto

# ------------------------------------------------------------------------------
def fora_desordeados(lst_elementos: List[str], lst_texto: List[str]) -> List[List[str]]:
    for tupla in lst_elementos[::-1]:
        if len(tupla) > 1:
            for ele1, ele2 in zip(tupla, lst_texto):
                if ele1.lower() != ele2.lower():
                    lst_elementos.remove(tupla)
                    break
    return lst_elementos

# ------------------------------------------------------------------------------

def sacar_variacions(entrada: str) -> List[str]:
    acentos = False
    #con = sqlite3.connect('alias_reservados.db')
    #cur = con.cursor()
    #print()

    #for ele in lst_saida:
        #cur.execute(f'insert into alias("valor_alias") values("{ele}")')

    #con.commit()
    #con.close()

    if unidecode(entrada) != entrada:
        acentos = True

    lst_permus, lst_texto = parecidos(entrada)
    lista = [' '.join(ele) for ele in lst_permus]
    lista += [unidecode(ele) for ele in lista]

    #lst_permus_ordeados = fora_desordeados(lst_permus.copy(), lst_texto)
    #lista_ordeados = [' '.join(ele) for ele in lst_permus_ordeados]
    #lista_ordeados += [unidecode(ele) for ele in lista_ordeados]

    lista_espaciada = [espaciar(ele) for ele in lista]
    return [ele for sublista in lista_espaciada for ele in sublista]

def main():
    cnf = cargarJson('./.cnf')

    con = sqlite3.connect(cnf['db'])
    cur = con.cursor()

    for ele in sacar_variacions(input('Nome do que sacar variacións: ')):
        try:
            cur.execute(f'insert or ignore into alias("valor_alias") values("{ele}")')
        except sqlite3.IntegrityError as e:
            raise e

    con.commit()
    con.close()

if __name__ == '__main__':
    print('Programa mal feito e con moitos bugs')
    while True:
        main()

# ------------------------------------------------------------------------------
