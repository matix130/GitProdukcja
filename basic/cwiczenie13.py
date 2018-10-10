#while True:
 #   a=input("Podaj temperaturę (Wpisz K aby zakończyć): ")
  #  if a=="K":
   #     break
    #    print(f"Średnia temperatura z {dni} dni wynosi: {wynik}")

suma_temperatur=0
i=0
while True:
    dane=input("Podaj")

    if dane=="k":
        break

    suma_temperatur += float(dane)
    i+=1
print("Średnia temperatura to: ", round(suma_temperatur/i,2))