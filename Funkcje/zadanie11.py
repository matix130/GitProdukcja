

# lista=[1, 2, 3, 4, 5, 6, 7]
# out=[False, False, False, True, True, True, False]
#
# def bigger_then_3(liczba):
#     if liczba > 3:
#         return True
#     return False
#
# def rowne_6(liczba):
#     if liczba == 6:
#         return True
#     return False
#
#
#
# assert out==[4,5,6]

def przytnij(data, start, stop):
    result=[]
    dodawac_do_listy=False
    for element in data:
        if start(element):
            dodawac_do_listy=True
        if dodawac_do_listy:
            result.append(element)
            if stop(element):
                break
    return result

def test_przytnij():
    assert przytnij(
        data=[1,2,3,4,5,6,7],
        start=lambda x: x>3,
        stop=lambda x: x==6
    )
