import sys
'''
firstname = sys.argv[1:]
#lastname = sys.argv[2]

email = str(firstname)+ "@deepideva.in"
print("\n----Yor Profile------")
print("Your Name: ",firstname)
#print("Your Last Name: ", lastname)
print("Your company email id is: ",email)
'''
'''
firstname = "".join(sys.argv[1:])
#lastname = sys.argv[2]

email = str(firstname)+ "@deepideva.in"
print("\n----Yor Profile------")
print("Your Name: ",firstname)
#print("Your Last Name: ", lastname)
print("Your company email id is: ",email)
'''
firstname = ".".join(sys.argv[1:])
#lastname = sys.argv[2]

email = str(firstname.lower())+ "@deepideva.in"
print("\n----Yor Profile------")
print("Your Name: ",firstname)
#print("Your Last Name: ", lastname)
print("Your company email id is: ",email)

