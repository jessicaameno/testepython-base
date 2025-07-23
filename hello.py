#!/usr/bin/env python3
 """ Hello Word Multi Linguas

Dependendo da lingua configurada no ambiente  o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamene ccinfigurada ex: 

    export LANG=pt_BR

Execuçao:

   python3 hello.py
   ou
   ./hello.py
"""
__version__ ="0.0.1"
__author__ = "Jessica"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG, "en_US")[:5]

msg =  "helo, word!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "hola, mundo!"
               
print (msg) 
