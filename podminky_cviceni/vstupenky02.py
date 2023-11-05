# Cena vstupenky


print("Divadlo pěst na oko" + "\n" + "Vítejte v online rezervaci vstupenek" + "\n" + "Pro vstup do systému je potřeba registrace" + "\n")
input("Zadejte Vaše uživatelské jméno: ")
vek = int(input("Zadejte Váš věk: "))

plna_cena = 12

if vek < 6:
    cena = 0
elif vek >= 6 and vek <= 26:
    cena =  round(plna_cena * 0.65)
elif vek >= 27 and vek <= 64:
    cena = round(plna_cena)
elif vek >= 65:
    cena = round(plna_cena * 0.5)

print(f"Cena vstupenky je {cena}.")

