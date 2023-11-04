# Ověřování hesla - bonus bonusu

import random

heslo = input("Zadejte heslo: ")

random1 = random.randint(1, len(heslo))
pozice = random1 - 1
znak = input("Zadej " + str(random1) + "." + "znak hesla: ")

if znak != heslo[pozice]:
  print("Chyba ověření.")
  exit()
random1 = random.randint(1, len(heslo))
pozice = random1 - 1
znak = input("Zadej " + str(random1) + "." + "znak hesla: ")
if znak != heslo[pozice]:
  print("Chyba ověření.")
  exit()
random1 = random.randint(1, len(heslo))
pozice = random1 - 1
znak = input("Zadej " + str(random1) + "." + "znak hesla: ")
if znak != heslo[pozice]:
  print("Chyba ověření.")
  exit()
print("Ověření bylo úspěšné!")