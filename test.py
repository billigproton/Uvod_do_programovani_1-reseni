import random
heslo = "SkakalPespresOves"
nahodne_cislo1 = random.randint(1,17)
znak = input (f"Zadej {nahodne_cislo1}.znak hesla: ")
if znak !=heslo[nahodne_cislo1 - 1]:
  print("Špatně")
  exit()
nahodne_cislo2 = random.randint(1,17)
znak = input(f"Zadej {nahodne_cislo2}.znak hesla: ")
if znak !=heslo[nahodne_cislo2 - 1]:
  print("Špatně")
  exit()
nahodne_cislo3 = random.randint(1,17)
znak = input(f"Zadej {nahodne_cislo3}.znak hesla: ")
if znak !=heslo[nahodne_cislo3 - 1]:
  print("Špatně")
  exit()
print("Vstup povolen")