import sys

try:
    print(sys.argv)
except IndexError:
    print("Zapomniałeś podać nazwę pliku")


with open(sys.argv[1]) as f:
    i=1
    for line in f:
        print(i, line, end="")
        i+=1
