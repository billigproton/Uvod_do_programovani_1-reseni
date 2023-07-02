# Délka názvu

nazev = "Pěst na oko"

delka = len(nazev)

print(delka)

pocet_cm = delka * 30

print(pocet_cm)


# Zaokrouhlování

eura = 12 * 0.65

koruny = round(eura * 24)

print(koruny)


# Zaoukrouhlování nahoru

import math

koruny = math.ceil(eura * 24)

print(koruny)


# Náhodná čísla

import random

cislo_predstaveni = random.randint(1, 24)

print(cislo_predstaveni)