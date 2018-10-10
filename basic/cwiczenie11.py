x=int(input("Podaj pozycję gracza X: "))
y=int(input("Podaj pozycję gracza Y: "))

if x>100 or x<0 or y>100 or y<0:
    wynik="Jesteś po za planszą!"

elif x<=10 and y<=10:
    wynik= "Lewy dolny róg"
elif 10<x<=90 and y<=10:
    wynik= "Dolna krawędź"
elif x>90 and y<=10:
    wynik= "Dolny prawy róg"
elif x<=10 and 10<y<=90:
    wynik= "Lewa krawędź"
elif x>90 and 10<y<=90:
    wynik= "Prawa krawędź"
elif x<=10 and y>90:
    wynik= "Lewy górny róg"
elif 10<x<=90 and y>90:
    wynik= "Górna krawędź"
elif x>90 and y>90:
    wynik= "Prawy górny róg"
else:
    wynik= "Centum"

print(f"Pozycja gracza to: {wynik}")