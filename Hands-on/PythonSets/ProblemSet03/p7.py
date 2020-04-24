def using_only(word,str_list):
    for char in word:
        if char not in str_list:
            return False
        else:
            return True

word=input('Enter word:')
sentence='acefhlo'
str_list=list(sentence)
print(using_only(word,str_list))