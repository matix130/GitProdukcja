#lista=[5,6,7]

#for x in lista:
  #  print(x)

#for x in range(11):
   # print(x)


#for idx, x in enumerate(lista):
 #   print(idx, x)


#Napisz program zliczjący wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb całkowitych

lista=[-5,-4,-3,-2,0,-1,1,2,3]

dodatnich=0
ujemnych=0

for x in lista:
    if x>0:
        dodatnich += 1
    elif x<0:
        ujemnych += 1

print(f"Dodatnich: {dodatnich} Ujemnych: {ujemnych}")