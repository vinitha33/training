def gcd(a,b):
    if a == 0:
        return "GCD is {}".format(b)
    elif b == 0:
        return "GCD is {}".format(a)
    elif a == b:
        return "GCD is {}".format(b)
    elif a > b:
        return gcd(a-b,b)
    return gcd(a,b-a)

num1 = int(input("Enter first no:"))
num2 = int(input("Enter second no:"))

print(gcd(num1,num2))
