import random

getal1 = random.randint(1,20)
getal2 = random.randint(1,20)
som = getal1 + getal2
#print(som)

print("Geef de som van", getal1,"en",getal2)
som_gebruiker = int(input())
#print(som_gebruiker)

if som_gebruiker == som:
    print("Correct")
    print("Goed bezig")
else:
    print("Niet correct")
    print("Niet Goed bezig")