# přestupný rok

rok = input("Zadejte rok: ")

if rok % 4 == 0 or (rok % 100 != 0 and rok % 400 == 0):
  print("Rok je přestupný.")
else:
  print("Rok není přestupný")


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