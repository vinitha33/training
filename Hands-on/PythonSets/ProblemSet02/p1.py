def GCD(a,b):
    if b<=a:
        rem = a%b
    if rem == 0:
        return "GCD is {}".format(b)
    else:
        return GCD(b,rem)

result = GCD(25,20)
print(result)