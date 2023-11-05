# přestupný rok

rok = int(input("Zadejte rok: "))

if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
  print("Rok je přestupný.")
else:
  print("Rok není přestupný")

rok = int(input("Zadejte rok: "))

if rok % 4 != 0:
  print("Rok není přestupný")
  exit()
# Zde využíváme vnořenou podmínku - podmínku uvnitř podmínky
if rok % 100 == 0:
  if rok % 400 == 0:
    print("Rok je přestupný.")
  else:
    print("Rok není přestupný")
else:
  print("Rok je přestupný.")

# Jirkova další varianta 

rok = int(input("Zadejte rok: "))
if rok % 4 != 0:
    # Např. rok 2023
    print("Rok není přestupný.")
    exit()
if rok % 100 == 0:
    if rok % 400 == 0:
        # Např. rok 2000
        print("Rok je přestupný")
    else:
        # Např. rok 1900, 2100
        print("Rok není přestupný")
else:
    # Např. rok 2024
    print("Rok je přestupný.")