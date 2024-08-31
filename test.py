uzivatelske_jmeno = input("Zadejte své uživatelské jménbo: ")
if uzivatelske_jmeno != "simsalabim":
    print("Vstup nepovolen")
    exit
vek = int(input("Zadej svůj věk: "))
if vek >= 18:
    print("Smíš vstoupit")
else:
    print("Vstup povolen od 18 let ")