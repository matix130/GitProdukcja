
class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie=imie
        self.nazwisko=nazwisko
        self.stawka=stawka
        self.godzina=0
        self.pay_day=0

    def register_time(self, godzina):
        self.godzina+=godzina

    def pay_salary(self):
        # if self.godzina <= 8:
        #     pay_salary = self.stawka * self.godzina
        #     print(f"Wypłata {pay_salary}")
        # else:
        #     pay_salary = self.stawka * 8 + 2 * self.stawka * (self.godzina - 8)
        #     print(f"Wypłata {pay_salary}")
        wyplata=self.stawka * self.godzina
        self.godzina = 0.0
        return wyplata
    # def zliczanie(self):
    #     self.pay_day+=self.pay_salary()
    #     print(f"Cała wypłata to {self.pay_day}")

employee=Employee("Jan", "Nowak", 100)
employee.register_time(5)
employee.pay_salary()
employee.register_time(10)
employee.pay_salary()

