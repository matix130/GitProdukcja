# zadanie 4 z tupli
liczby=0
a=int(input("Podaj ilość: "))
for x in range(a+1):
    if x%3==0 or x%5==0:
        liczby+=1
        print(x)

print(f"W przedziale 0-100 jest {liczby} liczb podzielnych przez 3 lub 5")