name=str(input("Enter Your Name: "))
print("Capitalized name is : ",name.capitalize())
print(name.lower())
print(name.upper())
print(len(name))
print(type(name))

mobile=str(input("Enter Your Mobile Number: "))
masked = mobile[:2] +"******"+mobile[-2:]
print("Your Mobile Number is: ", masked )
