# Jednoduchý vstup

jmeno_prijmeni = input("Zadejte Vaše jméno a příjmení: ")

vek = int(input("Zadejte váš věk: "))

 # další způsob zápisu
 
print(jmeno_prijmeni, vek, sep=", ")

 # kdyby jste nechtěli převádět věk na číslo

vek = input("Zadejte váš věk: ")

print(jmeno_prijmeni + ", " + vek)
