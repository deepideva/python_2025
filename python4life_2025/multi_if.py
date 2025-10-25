recharge =int(input("Enter Recharge amount : "))
data=float(input("Enter your needed data : "))
print("Bonus applied only for 399 Rs + or 2 GB +")
if recharge >= 399 or data >=2:
    print("Hey, You got 2 GB Bonus")
else:
    print("Not Eligible for Bonus")