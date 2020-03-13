#Convert capital letters to lower letters and vice versa without using built-in functions

str = input("Original string:")

# str1 = str.swapcase()
str1 = '';
for a in str:
    if a.isupper():
        str1 += (a.lower())
    elif a.islower():
        str1 += (a.upper())

print("Reversed Case :" + str1)

'''str2 = "".join(list((reversed(str1))))
str3 = str1[::-1]
print(str2)
print(str3)'''