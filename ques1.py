# ENTER your desired input
main_string = input("Enter the string :")
listing_string = list(main_string)
#below is the case when space is not in between strings
if " " not in listing_string:
    new_list = []
    for character in listing_string:
        if character not in new_list:
            new_list += character
    for i in new_list:
        print(f"count of {i} is : {listing_string.count(i)}")
else:
    new_list=main_string.split()
    created_list=[]
    for word in new_list:
        if word not in created_list:
            created_list.append(word)
    for i in created_list:
        print(f"count of {i}:{new_list.count(i)}")