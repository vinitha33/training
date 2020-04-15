b = []
for x in range(1,11):
    a = int(input("Enter number "+str(x)+": "))
    b.append(a)

c = []
d = []

for i in b:
    if i% 2 == 0:
        c.append(i)
        #print("None of them are odd numbers")
    else:
        d.append(i)

d.sort()
#count = 0

if len(d) == 0:
    print("None of them are odd numbers")
else:
    print("Largest odd number",d[-1])
