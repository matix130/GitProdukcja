

#def - definicja
def hello():
    print("Hello World") # definicja funkcji
    return 10

def hello2(name): # name to zmienna
    print(f"Hello {name}")


def hello3(name="World"):
    print(f"Hello {name}")


# print(type(hello))
#
# hello()
# hello2("Rafał")
# hello3("Mati")


def dodaj(a, b):
    return a + b


def test_dodaj_dwie_liczby():
    assert dodaj(1, 2) == 3


#
#
# x = print("testuje co zwraca print")
# print("x:", x)
# y= dir()
# print("y:", y)
#
# z= hello()
# print("z:", z)
#
#
# wynik= dodaj(10, 11)
# print(wynik)