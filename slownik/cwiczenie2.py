napis=input("Podaj napis: ").lower()

liczniki = {}
for litera in napis:
    if litera != " ":
        liczniki[litera] = liczniki.get(litera, 0) + 1

print(liczniki)