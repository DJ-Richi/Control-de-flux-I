# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Fes un programa que donat un número et digui si és par o inpar.
# Especificacions d'entrada: un numero que dono si es par o inpar.

try:
    # Demanar un número a l'usuari
    numero = int(input("Introdueix un número enter: "))
    
    # Comprovar si és parell o imparell
    if numero % 2 == 0:
        print(f"El número {numero} és PARELL")
    else:
        print(f"El número {numero} és IMPARELL")

# Si no intrudueixes un valor enter    
except ValueError:
    print("Error: Has d'introduir un número enter vàlid!")4