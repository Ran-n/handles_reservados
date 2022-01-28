#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/28 19:27:39.865485
#+ Editado:	2022/01/28 20:02:27.367501
# ------------------------------------------------------------------------------
import os
import sqlite3
from uteis.ficheiro import cargarFich, cargarJson
# ------------------------------------------------------------------------------
cnf = cargarJson('./.cnf')

db = cnf['db']

try:
    os.remove(db)
except OSError:
    pass

con = sqlite3.connect(db)
cur = con.cursor()

con.executescript(''.join(cargarFich(cnf['script_db'])))

con.commit()
con.close()
# ------------------------------------------------------------------------------
