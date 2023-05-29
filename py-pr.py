#a = "*"
#for i in range(5):
 #   for j in range(5):
  #      print('*',end=' ')
   # print('')
#print('')

#for i in range(5):
 #   for j in range(i+1):
  #      print('*',end=' ')
   # print('')
#print('')

#for i in reversed(range(5)):
 #   for j in range(i+1):
  #      print('*',end=' ')
   # print('')

    #a = int(input("zadaj 1. cislo. . ."))
    #b = int(input("zadaj 2. cislo. . ."))
    #c = int(input("zadaj 3. cislo. . ."))
    #V = ((a+b+c)/3)
    #print(V)

List = []
a = int(input("zadaj cislo: "))
while 1 :
    List.append(a)
    a = int(input("zadaj cislo: "))
    print(List)
    b = sum(List)
    c = len(List)
    if a == 0:
        print("priemer je. . .",b/c)
        break



import random
#a = random.randrange(1, 100)
#b = int(input("Zadaj cislo. . . "))

#while b != a:
    #if b > a:
        #print("Mensie cislo...")
    #else:
        #print("Vacsie cislo...")
    #b = int(input("znova: "))

#print("ok")