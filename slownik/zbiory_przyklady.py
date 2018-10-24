# suma |
# różnica -
#iloczyn &
# różnica symetryczna ^


zbior_a = {1,3,4,5,6}

zbior_a.add(7)
zbior_a.add(2)
print(zbior_a)
print(type(zbior_a))
print("="*30)
print()

lista=[1,1,2,2,3,3,4,4,5,5,6,6]
print(set(lista))
print("="*30)
print()

a = {1,2,3,4}
b = {4,5,6,7}

print("Suma a+b", a | b)
print("Różnica a-b", a - b)
print("Różnica b-a", b - a)
print("Iloczyn a*b", a & b)
print("Różnica symetryczna", a ^ b)
print("="*30)
print()

print(list(range(1,100,2)))
print("-"*195)
print(set(range(1,100,2)))
print("="*30)
print()

x={49,59,20,40,10,15}
y=set(range(1,100,2))
print("Część wspólna x oraz y: ", x&y)