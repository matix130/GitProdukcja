

class Animal: # lub class Animal():
    krolestwo="Fauna" # atrybut klasowy

    def __init__(self, nazwa):
        self.nazwa=nazwa

zyrafa = Animal() # tu trzeba uzyc dwoch nawiasow !!!
mysz=Animal() # instancja klasy (egzemplarz klasy)
print(type(zyrafa))
print(zyrafa.krolestwo)
print(mysz.krolestwo)

#atrybut klasowy moge zmodyfikować

Animal.krolestwo="Flora"

print(zyrafa.krolestwo)
print(mysz.krolestwo)


zyrafa.krolestwo="Fauna"

print(zyrafa.krolestwo)
print(mysz.krolestwo)