# Jednoduchý vstup

jmeno_prijmeni = input("Zadejte Vaše jméno a příjmení: ")

vek = input("Zadejte váš věk: ")

print(jmeno_prijmeni + ", " + vek)

 # další způsob zápisu
 
print(jmeno_prijmeni, vek, sep=", ")

 # formátovaný řetězec - ideální zápis :)

vek = int(input("Zadejte váš věk:"))

print(f"{jmeno_prijmeni}, {vek}")
