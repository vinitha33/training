a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("None of the numbers are odd")
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
elif a % 2 != 0 and b % 2 != 0:
    if a > b:
        print(a)
    else:
        print(b)
elif b % 2 != 0 and c % 2 != 0:
    if b > c:
        print(b)
    else:
        print(c)
elif c % 2 != 0 and a % 2 != 0:
    if c > a:
        print(c)
    else:
        print(a)
