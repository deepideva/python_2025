pwd = input("Enter your password : ")
check = input("Re-Enter your password : ")
while pwd != check:
    pwd=(input("Password mismatch, Try again : "))
    
print("Access Granted")