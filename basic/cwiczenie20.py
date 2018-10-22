#cwiczenie listy5
#x=[1,2,3,4]
# for i in x:
#   print(f"{i:3}", end="")
print("    ", end="")
for x in range(10):
    print(f"{x:3}",end="")

print("\n")


for x in range(10):
    print(x, end="   ")
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()