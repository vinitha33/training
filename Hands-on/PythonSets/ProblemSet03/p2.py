def rotate(s,num,low,high):
    str1=" "
    for i in s:
        if num>0:
            x=ord(i)+num
            if x>high:
                y=low+(x-high)
                str1+=chr(y-1)
            else:
                str1+=chr(x)
        else:
            x=ord(i)-abs(num)
            if x<low:
                y=high-(low-x)
                str1+=chr(y+1)
            else:
                str1+=chr(x)
    print(str1)
num=int(input())
string1=str(input())
if string1.isupper():
    rotate(string1,num,65,90)
else:
    rotate(string1, num,97,122)