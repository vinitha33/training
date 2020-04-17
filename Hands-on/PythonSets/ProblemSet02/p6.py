def findAnEven(l):
    for i in range(0,len(l)):
        try:
            if l[i] % 2 == 0:
                print(l[i])
                break
            elif i == len(l)-1:
                raise ValueError("List l does not contain an even number")
        except ValueError as e:
            print(e)
l = [3,2,21,10,1]
findAnEven(l)