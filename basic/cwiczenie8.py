a=int(input("Podaj szerokość podstawy opakowania w cm: "))
b=int(input("Podaj długość podstawy opakowania w cm: "))
h=int(input("podaj wysokość opakowania w cm: "))
V=(a*b*h)/1000
print(f"Objętość opakowania wynosi {V}L")
print(f"Opakowanie jest większe od jednego litra {V>1}")

if V>1:
    print("Objętość większa niż 1 litr")
else:
    print("Objętość mniejsza bądź równa litrowi")