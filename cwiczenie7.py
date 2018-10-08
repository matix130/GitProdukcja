a = int(input("Podaj liczbę: "))
print(f"Podzielna przez 2 i 3, większa od 10 lub jest to 7:"
      f" {a==7 or a%2==0 and a%3==0 and a>10}")
print
