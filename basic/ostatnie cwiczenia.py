import json
from threading import Thread

from urllib.request import urlopen
from time import sleep

from time import time

class MyThread(Thread):

    def run(self):
        with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
            print(file.read())
przed=time()

watki=[]
for i in range(10):
    watek = MyThread()
    watek.start()
    watki.append(watek)



for watek in watki:
    watek.join()
    
po=time()

czas=po - przed
print(f"Czas trwania {czas}s")






# class MyThread(Thread):
#     def __init__(self):
#         super().__init__()
#         pass
#     def run(self):
#         sleep(4)
#         print("Cześć")
#
# watek=MyThread()
# watek.start()
# print("Hej")
# watek.join()
