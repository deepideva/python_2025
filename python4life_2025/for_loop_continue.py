#To print positive numbers
n = [10,9,8,-7,-6,5,4,-3,-2,1,-7]
positive = 0
total = len(n)

for num in n:
    if num <= 0:
        continue
    print("Positive Numbers are : ",num)
    positive=positive+1
  
print("Total Count of Positive numbers are: ",positive)
print("Total Count of Positive and Negative are : ",total)