num1 = int(input("Enter how many numbers you want to enter:"))
a = []
b = []
e = []
for i in range(0,num1):
    x = int(input())
    a.append(x)

for i in range(0,num1):
    x = int(input())
    b.append(x)

try:
    for i in range(len(b)):
        if a[i]/b[i] != 0:
            e.append(a[i]/b[i])
        else:
            raise Exception()
    print(e)

except:
    print("An exception occured")
