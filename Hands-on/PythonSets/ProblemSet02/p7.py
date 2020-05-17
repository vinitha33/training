def isPalindrome(s):
    if len(s) <= 1:
        return True
    s2 = ""
    s2 = s1[::-1]
    if s1 == s2:
        return True
    else:
        return False

str1 = input("Enter the string:")
s1 = ""
for i in str1:
    if i.isalpha():
        s1 += i
s1 = s1.lower()
print(isPalindrome(s1))
