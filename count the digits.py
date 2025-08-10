# count the digits

n = int(input("Enter the number : "))
temp = n
count = 0
while temp > 0:

    count +=1
    temp //=10

print(f"the total number of digits in the no. {n} is {count}")