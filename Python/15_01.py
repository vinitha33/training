# Reverse the string except vowels (CAMEL -> LAMEC)

str1 = input("Enter the string:")
str2 = str3 = str4 = ""
j = 0
vowel_set = {"a", "e", "i", "o", "u"}
for i in range(len(str1)):
    if str1[i] not in vowel_set:
        str2 += str1[i]
        str3 = str2[::-1]

for i in range(len(str1)):
    if str1[i] not in vowel_set:
        str4 += str3[j]
        j = j + 1
    else:
        str4 += str1[i]

print(str4)


