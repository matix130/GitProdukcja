napis=input("Wpisz zdanie, aby zliczyć liczbę samogłosek: ")
i=0

samogloski='aeiouy'

for litera in napis:
     if litera in samogloski:
          i=i+1


print(i)