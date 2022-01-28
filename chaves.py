#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/27 18:42:07.263328
#+ Editado:	2022/01/28 21:11:44.494888
# ------------------------------------------------------------------------------
import secrets
import os
import sys
# ------------------------------------------------------------------------------
sistema_operativo = sys.platform

seguir = True
while seguir:
    if sistema_operativo == 'win32':
        os.system('cls')
    elif sistema_operativo == 'linux':
        os.system('clear')

    print()

    for i in range(1, 20):
        print(secrets.token_urlsafe(32)[:32])

    print()
    if input('Intro para máis chaves') == '.': seguir = False

# ------------------------------------------------------------------------------
