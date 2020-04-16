str1 = input("Enter first string:")
str2 = input("Enter second string:")

def isIn(str1,str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False

print(isIn(str1,str2))