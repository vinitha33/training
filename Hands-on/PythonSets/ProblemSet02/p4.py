num = 10011
b = 0
i = 0
while(num):
    ld = num % 10
    num = int(num / 10)
    b = b + ld * (2 ** i)
    i = i + 1
print(b)
