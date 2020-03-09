str1 = "aabcde"

str2 = str1*1000

count1 = 0
count2 = 0

for i in range(len(str2)):
    if str2[i] == "a":
        if str2[i+1] == "a":
            if str2[i+2] == "b":
                count1 = count1+1
    else:
        pass

print(count1)