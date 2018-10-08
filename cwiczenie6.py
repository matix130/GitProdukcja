a = float(input("Podaj liczbę: "))
print("Większa od 10: ", 10 < a)
print("Mniejsza równa 15: ", 15 >= a)
print("Podzielna przez 2: ", a % 2 == 0)

print(f"Podzielna przez 3 i większa od 10: ", a%2==0 and a>10)

print(f"Większa od 10 lub podzielna przez 5: {a>10 or a%5==0}")