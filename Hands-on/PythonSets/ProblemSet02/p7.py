def ispalindrome(s):
    x = "abcdefghijklmnopqrstuvwxyz"
    y = s.lower()
    s1 = ""
    for i in y:
        if i in x:
            s1 = s1 + i
    print(s1)
    s2 = s1[::-1]
    print(s2)
    if s1 in s2:
        print("Palindrome")
    else:
        print("Not Palindrome")
s = input()
ispalindrome(s)