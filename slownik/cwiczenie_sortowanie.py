lista = [5, 3, 4, 1, 2, 6]

print("Liczby przed: ", lista)

for indeks_podstawienie in range(len(lista)):
    indeks_minwartosci = indeks_podstawienie

    for indeks_ogona in range(indeks_podstawienie+1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_minwartosci]:
            indeks_minwartosci = indeks_ogona

    # value_temp = lista[indeks_minwartosci]
    # lista[indeks_minwartosci] = lista[indeks_podstawienie]
    # lista[indeks_podstawienie] =value_temp

    lista[indeks_minwartosci], lista[indeks_podstawienie] = lista[indeks_podstawienie], lista[indeks_minwartosci]

print("Liczby po: ", lista)

#assert lista == [1,2,3,4,5]