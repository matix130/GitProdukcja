a = int(input("Podaj rok urodzenia: "))
if 2018 - a >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")

import datetime
year = datetime.datetime.now().year
print(datetime.datetime.now())