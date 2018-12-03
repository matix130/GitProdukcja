lista = [1, 2, 3, 4]


try:
    print(lista[3])
except:
    print("Wystąpił jakiś błąd")
print("-"*30)

try:
    print(lista[3])
    list.add(5)
except IndexError as e:
    print("Próbujesz pobrać jakiś element spoza zakresu listy")
    raise IndexError
except AttributeError as e:
    print("Prawdopodobnie wywołujesz metodę, której ten obiekt nie ma")

print("-"*30)
print("aAAA")