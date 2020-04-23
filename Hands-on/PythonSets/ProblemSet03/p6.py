def avoid(list1,forbidden_str):
    for char in list1:
        count=0
        for letter in forbidden_str:
            if letter in char:
                count+=1
        if count==0:
            print(char)
string=str(input('Enter string:'))
list1=string.split(" ")
forbidden_str=str(input('Enter forbidden string:'))
avoid(list1,forbidden_str)