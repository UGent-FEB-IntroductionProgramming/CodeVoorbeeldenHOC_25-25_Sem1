import random

getal1 = random.randint(1,20)
getal2 = random.randint(1,20)

if getal2 > getal1:
    getal1, getal2 = getal2, getal1


verschil = getal1 - getal2
#print(som)

print("Geef verschil van", getal1,"en",getal2)
verschil_gebruiker = int(input())
#print(som_gebruiker)

while verschil_gebruiker != verschil:
    print("Niet correct")
    print("Niet Goed bezig")
    print("Geef verschil van", getal1,"en",getal2)
    verschil_gebruiker = int(input())
print("Correct")
print("Goed bezig")

