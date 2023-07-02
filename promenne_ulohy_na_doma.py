# Hrátky s porměnnými

 # A

velikost_souboru = 100

platy = velikost_souboru * 22392

print(platy)

 # B

studentske_vstupne = 0.6

nazev_predstaveni = "Proměna"

 # C

velikost_souboru = 102

platy = velikost_souboru * 22392

print(platy)


# Celočíselné dělení a dělení se zbytkem

 # A
  # se zbytkem
print(1024 / 72)
  # beze zbytku
print(1024 // 72)
  # zbytek po dělení
print(1024 % 72)

 # B

delka = 265

# C

hodiny = delka // 60

print(hodiny)

minuty = delka % 60

print(minuty)


# Sedačky v sále

celkem_sedacek = 350

rady_sedacek = 350 / 32

print(rady_sedacek) # vyjde nám zbytek => nebudou všechny řady stejně plné

 # kolik sedaček zbývá?

zbyva_sedacek = 350 % 32

print(zbyva_sedacek) 

 # kolik sedaček je potřeba dokoupit?

dokoupit = 32 - zbyva_sedacek

 # kolik nám po přikoupení vznikne řad sedaček?

celkem_rad = ((celkem_sedacek + dokoupit) / 32)

print(celkem_rad)



