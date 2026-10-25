temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(temperatures) / len(temperatures)
print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {min(temperatures)} / Max : {max(temperatures)}")

nb_jours_chauds = 0
for temperature in temperatures:
    if temperature > 15:
        nb_jours_chauds += 1
print(f"Jours > 15 °C : {nb_jours_chauds}")

temperatures_f = [round(c * 9 / 5 + 32, 1) for c in temperatures]
print(f"Fahrenheit : {temperatures_f}")

for i, temperature in enumerate(temperatures, start=1):
    print(f"Jour {i} : {temperature} °C")


    

