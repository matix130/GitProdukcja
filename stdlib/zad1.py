import json
try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy=[]


op=input("Co chcesz zrobić? [d - dodaj, w - wypisz] ")
if op == 'd':
    imie=input("Imie: ")
    nazwisko=input("Nazwisko: ")
    data=int(input("Data urodzenia: "))
    pensja=int(input("Pensja: "))
    pracownicy.append({"imie": imie, "nazwisko": nazwisko, "data": data, "pensja": pensja})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)

elif op == 'w':
    for nr, p in enumerate(pracownicy, 1):
        print(f" - [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['data']}, pensja: {p['pensja']} PLN ")