class Temperatura:
    def __init__(self, x):
        self.wartosc = x


    def __str__(self):
        return f"Temperatura: {self.wartosc} stopni Celcjusza."

x= Temperatura(20)
x.wartosc = -300
print(x)
