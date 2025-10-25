# Order amount 1000 + . If Sat , Sund , and Membership gold - bonus
from datetime import date
order_amount = int(input("Enter your Order amount to check for Offer: "))
day=date.today()
day_name=day.strftime("%A").lower()
print("Today Date is :",day_name)
member=str(input("Are you a Gold Member : (Enter y or n) : "))
if(order_amount >= 1000 and day_name in['saturday','sunday']) or member=='y':
    print("You are Eligible for Discount")
else:
    print("No Discount Applicable")

