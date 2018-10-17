#Lista
lista=[]

while len(lista)<10:
    x = input("Podaj liczbę lub k aby zakończyć: ")
    if x=="k" or x=="":
        break
    liczba=int(x)
    lista.append(liczba)
if len(lista) == 0:
    print("Nie podano danych!")
else:
    srednia=sum(lista)/len(lista)
    print(f"Średnia to {srednia}")