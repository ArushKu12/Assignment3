#assigning variable a value
number = 6

for i in range(number):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2 * (number - i) - 1):
        print(chr(65 + j), end='')
    print()