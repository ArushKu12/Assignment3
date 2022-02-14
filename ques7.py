#making variables
a = 0
b = 1
sum = 0
count = int(input("Enter the number of terms in fibonacci series: "))
if count == 1:
    print(a)
    sum=1
else:
    print(a)
    print(b)
    for i in range(2,count):
        c=a+b
        a=b
        b=c
        sum+=c
        print(c)
    sum+=1

print(f"The sum is {sum}")

average=sum/count

print(f"\nAverage is {average}")