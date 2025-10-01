# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 01/10/2024
# Versió: 1
#
# Descripció: Programa per comprovar si la persona es major o menor d'edat
# Especificacions d'entrada: Introduir l'any de naixement de la persona.

# Programa per calcular si ests menor d'edat o menor d'edat

# Demanar any de naixement
any_naixement = int(input("Introdueix el teu any de naixement: "))

# Obtenir l'any actual
from datetime import datetime
any_actual = datetime.now().year

# Calcular l'edat
edat = any_actual - any_naixement

# Determinar si és major d'edat
if edat >= 18:
    print(f"Tens {edat} anys. Ets MAJOR d'edat")
else:
    print(f"Tens {edat} anys. Ets MENOR d'edat")