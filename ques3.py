#asking the users for the required numbers
numbers = (input("Enter the numbers with ',' .between them :- ")).split(",")

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])


dictionary = {}
for i in numbers:
    dictionary[i] = i ** 2

making_tuple = dictionary.items()
print(making_tuple)