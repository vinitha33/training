num = input("Enter the number:")
a = []
k = 9

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if int(num[i]) + int(num[j]) == k:
            print(num[i],num[j])



