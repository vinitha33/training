a = str(input("Enter the string:"))

print(a)
vowel=['a','e','i','o','u']
count1=0
max=0
for i in a:
    if i in vowel:
        count1 = count1+1
        if max <= count1:
            max = count1
    else:
        count1 = 0
        pass

print(max)