#iteratory


class Iterator:
    def __init__(self, arg):
        self.arg=arg
        print(f"Tworze obiekt {arg}")



    def __iter__(self):
        self.licznik=0
        return self

    def __next__(self):
        if self.licznik > self.arg:
            raise StopIteration
        liczba=self.licznik
        self.licznik +=1
        return liczba

#
# for i in Iterator(16):
#     print(i)
class Vowels:
    def __init__(self, napis):
        self.napis = napis
    def __iter__(self):
        self.pozycja = 0
        return self
    def __next__(self):
        while self.pozycja < len(self.napis):
            litera=self.napis[self.pozycja]
            self.pozycja +=1
            if litera in "aeiouy":
                return litera
        raise StopIteration
for char in Vowels("ale"):
    print(char)





# lit=0
# samogloski="aeiouy"
# napis="ala ma kota a kot ma ale"
# for litera in napis:
#      if litera in samogloski:
#           pass
#
# print(lit)
# for i in Iterator(lit):
#      print(i)
