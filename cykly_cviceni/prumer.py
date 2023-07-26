# Vytvoření seznamu čísel
seznam_cisel = [3.5, 2.7, 6.8, 4.2, 5.1]

# Inicializace proměnných pro výpočet průměru
celkem_cisel = len(seznam_cisel)
soucet_cisel = 0

# Výpočet součtu čísel pomocí cyklu for
for cislo in seznam_cisel:
    soucet_cisel = soucet_cisel + cislo

# Výpočet průměru
prumer = soucet_cisel / celkem_cisel

# Výstup průměru
print("Průměr zadaného seznamu čísel je:", prumer)
