
zbior=set()
zbiorparz=set()
while True:
    liczby=input("Podaj liczbę. Wpisz k żeby zakończyć. ")
    if liczby == 'k':
        break
    else:
        liczby=int(liczby)
        zbior.add(liczby)
           # if liczby
        #zbiorparz.add(liczby)
print(zbior)
liczby_parzyste=set(range(0, 101, 2))
print(f"W tym liczb przystych od 0 do 100: {len(zbior & liczby_parzyste)}")