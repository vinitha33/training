def facti(f):
    p = 1
    for i in range(1,f+1):
        p = p * i
    print(p)
def factr(f):
    if f ==0 or f==1:
        return 1
    else:
        return f*factr(f-1)
f = int(input())
facti(f)
print(factr(f))