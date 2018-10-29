def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba%i==0:
            return False


    return True



def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(3)
    assert czy_pierwsza(67)



def test_czy_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(12)
    assert not czy_pierwsza(4)
    assert not czy_pierwsza(52)
