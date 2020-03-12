#To Check if two different strings has the same letters (Anagram)

str1 = input("Enter 1st String:")
str2 = input("Enter 2nd String:")

str3 = sorted(str1)
str4 = sorted(str2)

if str3 == str4:
    print("String have similar letters")
else:
    print("Doesnt have similar letters")