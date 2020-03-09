b_num = input("Enter the binary number:")

count1 = 0
max = 0
i = 0


for i in range(len(b_num)):

    if  b_num[i]=="0":
        count1=count1+1
        if max <= count1:
            max = count1
    elif b_num[i] == "1":
        # print(b_num[i])
        count1=0




print(max)

