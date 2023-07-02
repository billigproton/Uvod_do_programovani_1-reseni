import random

dolni_mez = int(input("Zadejte dolní mez: "))
horni_mez = int(input("Zadejte horní mez: "))

vygenerovane_cislo = random.randint(dolni_mez, horni_mez)

print(vygenerovane_cislo)
