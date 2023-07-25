jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if heslo != "simsalabim":
    print("Vstup nepovolen")
    exit()

vek = int(input("Zadejte váš věk: "))

if vek >= 18:
    print("Smíš vstoupit")

else: 
    print("Vstup povolen od 18 let")