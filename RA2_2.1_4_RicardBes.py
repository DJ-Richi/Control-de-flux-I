# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Programa per comprovar si una nota està aprovada o suspesa
# Especificacions d'entrada: Comprobar si el examen esta susspes o aprobat


# Demanar la nota a l'usuari
nota = float(input("Introdueix la nota de 1 a 10: "))

# Comprovar si la nota és vàlida i després si està aprovada
if nota >= 5 and nota <= 10:
    print("Aprovat")
elif nota >= 0 and nota < 5:
    print("Suspès")
else:
    print("Nota no vàlida! Ha de ser entre 0 i 10")