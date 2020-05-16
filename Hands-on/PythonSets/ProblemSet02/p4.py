num = int(input("Enter the number:"))
i = 0
final = 0
while num > 0:
    rem = num%10
    num = round(num/10)
    digit = pow(2,i) * rem
    final = final + digit
    i = i + 1
print(final)



