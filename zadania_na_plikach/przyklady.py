
#Otworzenie pliku do odczytu
with open("dane/input.txt") as f: #context manader
    for linia in f:
        print(len(linia))



# tylko do odczytu

with open("info.txt", "w", encoding='utf8') as f:
    for i in range(10):
        f.write(f"Jakiś test\n")


# with open("info.txt", "a", encoding='utf8') as f:
#     f.write("inny tekst")