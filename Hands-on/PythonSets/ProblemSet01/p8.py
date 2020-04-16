
n = int(input("Enter how many numbers you want to enter?"))
b = []
d = []
for x in range(0,n):
    a = int(input())
    b.append(a)

for x in range(0,n):
    c = int(input())
    d.append(c)
e=[]
try:
    for i in range(0,len(b)):
        if b[i]/d[i]!=0:
            e.append(b[i]/d[i])

        else:
            raise Exception('gujgfv')
    print(e)

except:
    print("An exception occurred")



