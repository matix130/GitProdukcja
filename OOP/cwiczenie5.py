from random import randint
from przedmiot import Przedmiot
#randint(1, 6) #losowa liczba z przedziału 1-6

class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek=[]


   # def przedstaw_sie(self):
     #   print(f"{self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.")

    @property
    def atak(self):
        wynik = self._atak
        for p in self.ekwipunek:
            wynik += p.bonus_atk
        return wynik

    def __str__(self):
        napis="EKWIPUNEK:\n"
        for x in self.ekwipunek:
            napis+=str(x) + "\n"
        return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia."


    def obrazenia(self, ile):
        if ile==self.zdrowie:
            self.zdrowie=0
            print(f"Nie żyjesz {self.imie}")
        elif ile>self.zdrowie:
            self.zdrowie=0
            print(f"Nie żyjesz {self.imie}")
        elif ile<self.zdrowie:
            self.zdrowie-=ile
            print(f"Otrzymałeś {ile} obrażeń i masz {self.zdrowie} życia.")


    def czy_zyje(self):
        if self.zdrowie > 0:
            print(f"Żyje i mam {self.zdrowie} życia")
        else:
            print("Nie żyje")

    def czy_zyje2(self):
        return self.zdrowie>0



    def leczenie(self, ile):
        if self.zdrowie==0:
            print(f"Nie żyjesz. Za późno na leczenie.")
        elif self.zdrowie+ile>self.max_zdrowie:
            self.zdrowie=self.max_zdrowie
        else:
            self.zdrowie+=ile

    def wskrzeszenie(self):
        if self.czy_zyje2():
            self.zdrowie=self.max_zdrowie
            print(f"Wskrzeszono mnie")

    def moc_ataku(self):
        wynik=randint(self.atak // 2, self.atak)
        return wynik

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)



    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje2() and broniacy.czy_zyje2():
            print(atakujacy)
            print(broniacy)
            print("I" * 30)
            atak_atakujacego=atakujacy.moc_ataku()
            atak_broniacy = broniacy.moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń.")
            broniacy.obrazenia(atak_atakujacego)
            print("v" * 30)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {atak_broniacy} obrażeń.")
            atakujacy.obrazenia(atak_broniacy)
            print("-"*30)
            print("-" * 30)
        print("Koniec walki")



minsc = Postac("Minsc", 30, 100)
korgan = Postac("Korgan", 40, 120)
tulipan= Przedmiot("Zielony tulipan zniszczenia", 5)
minsc.daj_przedmiot(tulipan)
Postac.walka(minsc, korgan)


#print(f"bonus: {minsc.atak()}")
print(minsc)
print(korgan)
print(tulipan)

# # rhino.przedstaw_sie()
# # print(rhino)
# minsc.przedstaw_sie()
# minsc.obrazenia(10)
#
# minsc.czy_zyje()
# minsc.obrazenia(89)
# minsc.leczenie(10)
# minsc.czy_zyje()
# minsc.wskrzeszenie()
# minsc.czy_zyje()

