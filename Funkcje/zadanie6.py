print("zadanie6")
def formatuj(*args, **kwargs):
    tekst = "\n".join(args)
    for k in kwargs:
        teskt =  tekst.replace("$"+k, str(kwargs[k]))
    return tekst

def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kowta $cena brutto',
        cena = 10,
    )== "koszt 10 PLN\n kwota 10 brutto"