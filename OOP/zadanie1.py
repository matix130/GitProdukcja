
class Produkt():
    def __init__(self, ID, produkt, cena):
        self.ID=ID
        self.produkt=produkt
        self.cena=cena

    def print_info(self):
        print(f"Produkt o numerze id {self.ID} to {self.produkt}, w cenie {self.cena}")

obiekt=Produkt("1", "Woda", 10.99)
obiekt2=Produkt("2", "Piwo", 11.98)
obiekt.print_info()
obiekt2.print_info()
