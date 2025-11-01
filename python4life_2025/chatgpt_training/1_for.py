'''for i in range(3):
    print("Hi")'''

'''
for n in range(2,5):
    print(n)'''  

'''count=1
while count <= 3:
    print(count)
    count += 1'''

'''for i in range (1, 6):
    if i ==3:
        break
    print(i)'''

'''for i in range(1, 6):  # i will take values: 1,2,3,4,5
    if i == 3:         # when i is 3
        continue       # skip the rest of the loop (skip print)
    print(i)           # print only if i is NOT 3
'''

count =0
while count < 5:
    count +=1
    if count == 2 or count == 4 :
        continue
    print(count)