from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from maths.models import Math


def obliczenia(request, dzialanie, zmienna1, zmienna2):
    z1=int(zmienna1)
    z2=int(zmienna2)
    wynik=None
    if dzialanie=="dodawanie":
        wynik=z1+z2
    elif dzialanie=="odejmowanie":
        wynik=z1-z2
    elif dzialanie=="mnozenie":
        wynik=z1*z2
    elif dzialanie=="dzielenie":
        if z2==0:
            return HttpResponse("Nie dziel cholero przez zero!")
        else:
            wynik=z1/z2

    m = Math(operacja=dzialanie, a=z1, b=z2, wynik=wynik)
    m.save()
    return HttpResponse(f"Twój wynik to {wynik}")