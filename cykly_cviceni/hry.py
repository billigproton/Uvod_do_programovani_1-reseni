# Hry

hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 165],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]

# A

for hra in hry:
   print(hra[0])

# B

for hra in hry:
    if hra[1] > 120:
        print(hra[0])



# C



for hra in hry:
    hodiny = str(hra[1] // 60)
    minuty = str((hra[1] % 60))
    print(hra[0] + " trvá " + hodiny + " h " + "a " + minuty + " min")