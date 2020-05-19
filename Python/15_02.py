# Count the occurence of 101 in a binary number

num1 = int(input("Enter the binary number:"))
count = 0
while num1 != 0:
    if num1 % 1000 == 101:
        count += 1
        num1 = int(num1/100)
    else:
        num1 = int(num1/10)
print(count)