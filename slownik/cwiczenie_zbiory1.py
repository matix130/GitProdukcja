
zbior=set()
while True:
    liczby=input("Podaj liczbę. Wpisz k żeby zakończyć. ")
    if liczby == 'k':
        break
    else:
        liczby=int(liczby)
        zbior.add(liczby)

print(zbior)