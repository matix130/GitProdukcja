from random import randint

graczX = randint(1, 10)
graczY = randint(1, 10)
skarbX = randint(1, 10)
skarbY = randint(1, 10)
print(f"Jesteś na X{graczX}, Y{graczY}. Szukaj skarbu! Tylko nie spadnij!")
print(f"Skarb jest na X{skarbX}, Y{skarbY}.")

while True:
    gracz = input("Podaj kierunek(W,A,S,D): ")

    if gracz == "w":
        graczY = graczY + 1
    elif gracz == "s":
        graczY = graczY - 1
    elif gracz == "a":
        graczX = graczX - 1
    elif gracz == "d":
        graczX = graczX + 1



    minKrokow = abs(skarbX - graczX) + abs(skarbY - graczY)
    if 1 > graczX or graczX > 10 or 1 > graczY or graczY > 10:
        print("Spadłeś!")
        break
    if graczX == skarbX and graczY == skarbY:
        print("Brawo znalazłeś skarb!")
        break
    elif 1 <= graczX or graczX <= 10 or 1 <= graczY or graczY <= 10:
        print(f"Jesteś na {graczX}, {graczY}. Szukaj dalej!")
      #  print(f"Brakuje {minKrokow} kroków")

  #  roznicaX = abs(graczX - skarbX)
   # roznicaY = abs(graczY - skarbY)
  #  if roznicaX < 2 or roznicaY < 2:
   #     print("Jesteś blisko")

