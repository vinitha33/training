#Diplay all the numbers which are greater than that number and are to the right side to it.

num1 = [10,4,2,5,3,6]
num2 = []
for i in range(len(num1)):
    for j in range((i + 1),len(num1)):
        if num1[i] < num1[j]:
            # num2.append(num1[i])
            num2.append(num1[j])
    if len(num2) == 0:
        print(num1[i],"= 0")
    else:
        print(num1[i],"=",num2)
    num2.clear()






