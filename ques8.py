#making 3 dictionaries
set_1 = {1, 2, 3, 4, 5}

set_2 = {2, 4, 6, 8}

set_3 = {1, 5, 9, 13, 17}
# solution to part a)
new_set_1 = set_1 ^ set_2
print(new_set_1)
# solution to part b)
a = set_1 - set_2
b = a - set_3

c = set_2 - set_1
d = c - set_3

e = set_3 - set_1
f = e - set_2

new_set_2 = b | d | f
print(new_set_2)
# solution to part c)
a = (set_1 | set_3) - set_2

b = (set_1 | set_2) - set_3

c = (set_2 | set_3) - set_1
new_set_3 = a | b | c
print(new_set_3)
# solution to part d)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
new_set_4 = a - set_1
print(new_set_4)
# solution of part e)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = a - set_1
new_set_5 = b - (set_2 & set_3)
print(new_set_5)