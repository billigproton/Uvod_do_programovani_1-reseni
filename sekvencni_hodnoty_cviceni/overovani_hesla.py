# Ověřování hesla

heslo = input("Zadejte vaše heslo: ")

druhy_znak = input("Zadejte 2. znak hesla: ")
paty_znak = input("Zadejte 5. znak hesla: ")
sesty_znak = input("Zadejte 6. znak hesla: ")

if druhy_znak != heslo[1]:
    print("Vstup zamítnut")

elif paty_znak != heslo[4]:
    print("Vstup zamítnut")

elif sesty_znak != heslo[5]:
    print("Vstup zamítnut")

else:
    print("Vstup povolen")