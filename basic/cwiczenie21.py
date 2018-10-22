liczby = [5,2,1,4,3]

min_ = liczby[0]
max_ = liczby[0]

for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

print(min_, max_)
print(liczby.index(min_), liczby.index(max_))
print(liczby)

print("Po zamianie")
liczby[liczby.index(min_)]=max_
liczby[liczby.index(max_)]=min_
print(liczby)