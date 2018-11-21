

def bold(funk):
    def wraper(*args, **kwargs):
        wynik = funk(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wraper

def italic(funk):
    def wraper(*args, **kwargs):
        wynik = funk(*args, **kwargs)
        return "<i>" + wynik + "<\\i>"
    return wraper
@bold
@italic
def nasza_funckja():
    return "jakaś funkcja"

print(nasza_funckja())