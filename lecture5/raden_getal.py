import random

te_raden_getal = random.randint(1,100)

getal = int(input("geef je getal?"))

while getal != te_raden_getal:
    if getal < te_raden_getal:
        print("Het getal dat je zoekt is groter")
    else:
        print("Het getal dat je zoekt is kleiner")
    getal = int(input("geef je getal?"))

print("Correct getal gevonden")

#print(te_raden_getal)