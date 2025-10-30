items = []
while True:
    inp = input("Enter your Items (Finally add done once items added) : ")
    if inp.lower() == 'done':
        break
    items.append(inp)

print("Items in Cart are :",items)