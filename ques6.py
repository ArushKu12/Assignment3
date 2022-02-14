# creating a dictionary for storing data
sid_dictionary = {}
choice = input("Would to like to add another entry in the dictionary? (Y or N): ").upper()
while choice == "Y":
    sid = int(input("Enter SID:"))
    name = input("enter the name: ")
    sid_dictionary[sid] = name
    choice = input("Would to like to add another entry in the dictionary? (Y or N)").upper()
# solution of a)
print(sid_dictionary)
# solution of b)
print("\nsorted by names:")
sorting = sorted(sid_dictionary.items(), key=lambda x: x[1])
print(dict(sorting))
# solution to c)
print("\nsorted by sid:")
sorting_2 = sorted(sid_dictionary.items())
print(dict(sorting_2))
# solution to part d)
ask_sid = int(input("\nEnter the SID of student you are looking for :\n"))
print(f"The name of student is {sid_dictionary[ask_sid]}")