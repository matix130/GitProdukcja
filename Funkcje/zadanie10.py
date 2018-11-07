lista = [1,2,3,4,5,6]

#warunek jest tki że >3

out = [False, False, False, True, True, False]

def bigger_then_3(liczba):
    if liczba > 3:
        return True
    return False

def smaller_then_3(liczba):
    if liczba < 3:
        return True
    return False





def sprawdzam_czy_wieksze_niz_3(lista):
    out = []
    for element in lista:
        #if element > 3:
         #   out.append(True)
        #else:
        #    out.append(False)
        out.append(bigger_then_3(element))
    return out


def sprawdzam_czy(lista, warunek):
    # if element > 3:
    #   out.append(True)
    # else:
    #    out.append(False)
    for element in lista:
        out.append(warunek(element))
    return out

assert sprawdzam_czy_wieksze_niz_3(lista) == out
assert  sprawdzam_czy(lista, bigger_then_3) == out