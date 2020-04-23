def has_no_e(list1):
    list2=[]
    count=0
    for i in list1:
        if "e" in i:
            list2.append(i)
    print((len(list2)/len(list1))*100)
str1=str(input())
list1=str1.split(" ")
has_no_e(list1)