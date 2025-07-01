#NESTED LOOP

#1. CONTOH 1 : 
#for loop : 
for i in range(5):
    for j in range(6):
        print(j+1, end=' ')
    print()

#while loop : 
i = 1
while i <=5 : 
    j = 1
    while j <= 6 :
        print(j, end=' ')
        j = j+1
    print()
    i = i+1

#2. CONTOH 2 :
#for loop :
for i in range(6):
    for j in range (0,i+1):
        print(j+1, end=' ')
    print()

#while loop : 
i = 1
while i <= 6 : 
    j=1
    while j <= i :
        print(j, end=' ')
        j = j+1
    print()
    i = i+1