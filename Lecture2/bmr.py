# https://dodona.be/en/courses/4793/series/54610/activities/1071623231
mass_in_kg = int(input("mass in kg: "))
body_length_in_cm = int(input("height in cm: "))
age_in_years = int(input("age in years: "))

value4 = 66.4730 + (13.7516 * mass_in_kg) + (5.0033 * body_length_in_cm) - (6.7550 * age_in_years)
value5 = 655.0955 + (9.5634 * mass_in_kg) + (1.8496 * body_length_in_cm) - (4.6756 * age_in_years)

value6 = (value4/230)
value7 = (value5/230)

print("Een man moet dagelijks " + str(value6) + " chocoladerepen eten om zijn gewicht te behouden. Een vrouw moet dagelijks " + str(value7) + " chocoladerepen eten om zijn gewicht te behouden.")
