jmeno = input("Zvolte si uživatelské jméno: ")
heslo = input("Zvolte si heslo: ")
heslo_znova = input("Zadejte heslo znova: ")

if heslo != heslo_znova:
    print("hesla se neshodují!")
elif len(heslo) < 8:
    print("Pozor! Heslo má méně než 8 znaků..")
