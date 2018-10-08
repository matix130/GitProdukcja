a = input("Miasto A: ")
b = input("Miasto B: ")
c = float(input(f"Dystans {a}-{b}: "))
d = float(input("Cena paliwa: "))
e = float(input("Spalanie na 100 km: "))
koszt = (c / 100) * d * e
koszt = round(koszt, 2)
print(f"Koszt przejazdu {a}-{b} to", koszt, "PLN")
