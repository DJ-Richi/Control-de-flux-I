# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Fes un programa que donat un número et digui quin es el mes gran.
# Especificacions d'entrada: Trobar el número més gran entre tres números utilitzant l'and.


# Demanar tres números a l'usuari
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
num3 = float(input("Introdueix el tercer número: "))

# Trobar el número més gran
if num1 >= num2 and num1 >= num3:
    mes_gran = num1
elif num2 >= num1 and num2 >= num3:
    mes_gran = num2
else:
    mes_gran = num3

# Mostrar el resultat
print(f"El número més gran és: {mes_gran}")