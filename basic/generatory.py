samogloski="aeiouy"
napis="ala ma kota a kot ma ale"
def wypisz_samogloski(napis):
    for i in napis:
        if i in samogloski:
            yield i

for i in wypisz_samogloski(napis):
    print(i)







#
#
# def generator(jakismax):
#     for i in range(0, jakismax, 2):
#         yield i
#
#
# for x in generator(15):
#     print(x)
#


