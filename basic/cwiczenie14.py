znaleziona_max = None
znaleziona_min = None
while True:
    wejscie=input("Podaj liczbę: ")

    if wejscie == "koniec":
        break

    x = int(wejscie)
    y= int(wejscie)
    if znaleziona_max is None or x > znaleziona_max:
        znaleziona_max = x
    if znaleziona_min is None or y<znaleziona_min:
        znaleziona_min = y

if znaleziona_max is None:
    print("Nie wprowadzono danych")

print("Największa podana liczba to: ", znaleziona_max)
print("Najmniejsza podana liczba to: ", znaleziona_min)