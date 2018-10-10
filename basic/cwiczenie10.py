a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
x=input("Podaj rodzaj operacji: ")

if x == '+':
    print(f"Wynik: {a+b}")
elif x=='-':
    print(f"Wynik: {a-b}")
elif x=='*':
    print(f"Wynik: {a*b}")
elif b==0 and x=='/':
    print("NIE DZIEL CHOLERO PRZEZ ZERO!!!")
elif b!=0 and x=='/':
    print(f"Wynik: {a/b}")

# Druga metoda

if x == '+':
    wynik=a+b
elif x=='-':
    wynik = a - b
elif x=='*':
    wynik = a * b
elif b==0 and x=='/':
    print("NIE DZIEL CHOLERO PRZEZ ZERO!!!")
elif b!=0 and x=='/':
    wynik = a / b
if b!=0:
    print(f"Wynik operacji wynosi: {wynik}")