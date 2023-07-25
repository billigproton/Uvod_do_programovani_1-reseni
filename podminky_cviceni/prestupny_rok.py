rok = int(input("Zadejte kalendářní rok: "))

if rok % 4 == 0 or (rok % 100 == 0 and rok % 400 == 0) :
    print("Tento rok je přestupný")
else: 
    print("Tento rok není přestupný")


