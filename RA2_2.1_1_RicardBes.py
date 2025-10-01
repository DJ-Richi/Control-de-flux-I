# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Fes un programa que donat un número et digui si és més gran o no que zero.
# Especificacions d'entrada: un numero que dono major, menor o igual a 0

# Programa per comprovar si un número és positiu, negatiu o zero

# Demanar un número a l'usuari
numero = float(input("Introdueix un número: "))

# Comprovar el número utilitzant if, elif i else
if numero > 0:
    print(f"El número {numero} és MÉS GRAN que zero")
elif numero < 0:
    print(f"El número {numero} és MÉS PETIT que zero")
else:
    print(f"El número {numero} és IGUAL a zero")