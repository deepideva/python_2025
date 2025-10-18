dress = int(input("Enter Dress Price:  "))
tax = dress * 0.18
total = dress + tax
print("GST is", tax)
print("Total amount is :",total)


if dress >= 1000:
    discount = total * .10
    total -= discount
    print("Total Discount applied",discount, "Rupees")
    print("Your Discounted amount is: ",total)

else:
    print("Your Total amount is (Including GST)", total)
    print("Order is less than 1000 Rs, so no discount applied")


