a = str(input("Enter the string:"))

print(a)
vowel=['a','e','i','o','u']
count1=0
for i in a:
    if i in vowel:
        pass
    else:
        count1=count1+1

print(count1)