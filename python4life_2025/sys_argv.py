import sys

firstname = sys.argv[1]
lastname = sys.argv[2]

email = firstname.lower()+"."+lastname.lower()+"@deepideva.in"
print("\n----Yor Profile------")
print("Your Firstname: ",firstname)
print("Your Last Name: ", lastname)
print("Your company email id is: ",email)
