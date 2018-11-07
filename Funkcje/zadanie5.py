def fooo (pierwszy, *reszta):
    if reszta:
        return pierwszy + reszta[-1]
    return pierwszy

print(fooo(1))

print(fooo(1, 2))

print(fooo(1, 2, 5, 10))

fooo(1, 2, 5, 10, 20)

reszta = [1, 3, 7]
print(*reszta)

print(fooo(*reszta))

print("-"*30)

def druga_funkcja(**slownik):
    if 'd' in slownik:
        return slownik['a'] + slownik['d']

    return slownik['a']


print(druga_funkcja(a=2))
print(druga_funkcja(a=2, b=2, c=3, d=4))
print(druga_funkcja(a=2, b=2, c=3, d=14, zosia=15))

print("-"*30)

co_na_co = {
    "Ala": "Kot",
    "kota": "Alę"
}

def zamien(jakis_tekst, **co_na_co):
    for klucz in co_na_co:
        jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
    return jakis_tekst

print(zamien("Ala ma kota", **co_na_co))
print("-"*30)

napis="Ten $produkt kosztuje $cena"
napis2="Zajęcia z $przedmiot zostały odwołane"

def formatuj(napis, **CoNaCo):
    for slowo in CoNaCo:
        napis=napis.replace("$"+slowo, CoNaCo[slowo])
    print(napis, *CoNaCo)
    return napis



assert formatuj(napis, produkt="Samochód", cena="200000") == "Ten Samochód kosztuje 200000"
#assert formatuj(napis2,przedmiot="Fizyki") == "Zajęcia z Fizyki zostały odwołane"
