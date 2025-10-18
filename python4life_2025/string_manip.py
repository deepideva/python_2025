song = "Show me the meaning"
artist = "backstreetboys"
formatted = f"{song.title()}-{artist.title()}"
print(formatted)

location = "Chennai Central"
fxd_location= location.replace("Chennai Central","Tambaram")
print(fxd_location)

msg="Your Travel reference number is:  80154, Have Safe Travel"
print(msg)
my_id=msg.split(":")[1].split(",")[0].strip()
print(my_id)
if "Travel" in msg:
    print("Yes Travel In Progress")
print("Position of Reference is: ",msg.find("Travel"))

my_name="ganesh babu"
initials = [word[0].upper() for word in my_name.split()]
print(initials,"###Words printed in List")

my_name="ganesh babu"
initials = "".join([word[0].upper() for word in my_name.split()])
print(initials,"###Words came out from list and Joined ")

my_name="ganesh babu"
initials = " ".join([word[0].upper() for word in my_name.split()])
print(initials,"###Words came out from list and Joined, With 1 space ")

dirty_input="    Ganeshbabu   "
clean=dirty_input.strip()
print(clean)

word1="I am living in Thiruporur, Happily living ,my life"
length=len(word1)
print("Length of Total Sentence is: ",length)
split_len=len(word1.split(","))
#It will check words present before and after the comma
print(f"Word Count before and after , is: ",{split_len})
