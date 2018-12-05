
class Produkt():
    def __init__(self, ID, produkt, cena):
        self.ID=ID
        self.produkt=produkt
        self.cena=cena

    def print_info(self):
        print(f"Produkt o numerze id {self.ID} to {self.produkt}, w cenie {self.cena}")

    def dej_cene(self):
        return self.cena

class BasketEntry:
    def __init__(self, product, quantity):
        """

        :param product:
        :param quantity:
        """


class Basket:
    def __init__(self, ID, produkt, cena):
        self.ID = ID
        self.produkt = produkt
        self.cena = cena
        self.koszyk=0

    def add_prod(self, ilosc):
        self.koszyk+= ilosc

    def total_price(self):
        kwota= self.cena * self.koszyk
        print(f"Kwota {kwota}")
    def gen_basket(self):
        pass

koszyk = Basket(1, "Woda", 8)
koszyk.add_prod(5)
koszyk.total_price()
koszyk.gen_basket()