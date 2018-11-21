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