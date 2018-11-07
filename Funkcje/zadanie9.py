def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
    return out


lista=[1, 2, 3, [4, 5,[6, 7]], 7]

def test_splaszcz_zagniezdzone_listy():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]


lista2=[1, 2, 3, [4, 5,[6, 7]], 7]

def test_splaszcz_zagniezdzone_listy2():
    lista2 = [1, 2, 3, [4, 5, [6]], 7]
    assert splaszcz(lista2) == [1, 2, 3, 4, 5, 6, 7]