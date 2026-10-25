for temperature in [-3, 0, 15, 31]:
    if temperature < 0:
        categorie = "gel"
    elif temperature < 15:
        categorie = "froid"
    elif temperature < 25:
        categorie = "doux"
    else:
        categorie = "chaud"
    print(f"{temperature} °C : {categorie}")

print()

for annee in [2024, 1900, 2000]:
    est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
    if est_bissextile:
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")

    