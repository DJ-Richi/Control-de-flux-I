# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Programa per determinar si es una vocal o una consonant de l'abecedari.
# Especificacions d'entrada: Introduir una lletra per determinar si es una vocal o una consonant.

# Programa per determinar si una lletra és vocal o consonant

# Demanar una lletra a l'usuari
lletra = input("Introdueix una lletra: ")

# Comprovar si és vocal o consonant
if lletra in a or e or i or o or u:
    print(f"'{lletra}' és una VOCAL")
else:
    print(f"'{lletra}' és una CONSONANT")