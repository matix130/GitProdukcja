


def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('ala ma kota a kot ma ale') == 0

def test_policz_znaki_jeden_poziom_zaglebienia():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomow_zaglebienia_niestandardowe_znaczniki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('ala [kota [a kot]] ma [ale]', start='[', end= ']') == 18

def test_policz_znaki_niestandardowe_znaczniki_wiele_poziomow():
    assert policz_znaki('a <a<a<a>>>') == 6