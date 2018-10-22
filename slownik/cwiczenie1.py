produkty = {"ziemniaki":2, "pomidory":3, "marchewki":4}

print("W nsazym sklepie oferujemy: ")

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

print()
wybor_produktu=input("Który produkt chcesz kupić? ")
ile=input(f"Ile chcesz kupić [{wybor_produktu}]")
cena=int(ile) * produkty[wybor_produktu]
print(f"Zapłacisz {cena}")