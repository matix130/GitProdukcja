import re

regex=re.compile("\d{2}-\d{3}")
wynik=regex.findall("gktestklsfdlkte567-456stewfd03-015sklj55-889test")


regex_mail=re.compile("\w+@\w+\.com|\w+@\w+\.pl|\w+@\w+\.\w+\.pl")

wynik2=regex_mail.findall("fkjdhkh@onet.pljfdjod@o2.pl")

regex_data=re.compile("\d{2} [A-Z][a-z]{2} \d{4}")

wynik3=regex_data.findall("30 Jan 1994 15 Jun 2012 12 Elo 1998")

print(wynik)
print(wynik2)
print(wynik3)