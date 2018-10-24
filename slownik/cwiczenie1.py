produkty = {"ziemniaki":2, "pomidory":3, "marchewki":4, "piwo":2.5}
cena_ogolna=0
koszyk={}
magazyn = {"ziemniaki":10, "pomidory":10, "marchewki":10, "piwo":10}
print("W naszym sklepie oferujemy: ")

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

while True:
    wybor_produktu=input("Który produkt chcesz kupić? ")
    if wybor_produktu == "Koniec":
        print("=" * 30)
        print("Twój koszyk:")
        break
    if wybor_produktu in produkty: #and magazyn[wybor_produktu]<0:
        ile=int(input(f"Ile chcesz kupić [{wybor_produktu}]"))
        if ile <= magazyn[wybor_produktu]:
            koszyk[wybor_produktu] = ile
            magazyn[wybor_produktu] -= ile
        else:
            print(f"Nie mam tyle. Pozostało [{magazyn[wybor_produktu]}]")
        cena=ile * produkty[wybor_produktu]
        cena_ogolna = cena + cena_ogolna
        koszyk[wybor_produktu] = ile
    else:
        print("Sorry nie ma tego produktu!")

sumarycznie=0
for produkt in koszyk:
    cenaa= koszyk[produkt] * produkty[produkt]
    print(f"- {produkt} [{koszyk[produkt]}]: {cenaa} PLN")
    sumarycznie+=cenaa
print(f"Zapłacisz {cena_ogolna} PLN")
