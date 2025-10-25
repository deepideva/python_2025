age = int(input("Enter your age: "))
lic = str(input("Do you have License:  (Enter Y or N) "))
license=lic.lower()
#print(license)
if age >= 18:
    if license == 'y':
        print("You can Drive")
    else:
        print("Go and Apply for License")
else:
    print("Apply after 18")



    


