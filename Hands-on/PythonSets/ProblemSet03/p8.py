def is_abecedarian_fun(word):
    count=0
    print(word)
    list1=list(word)
    for i in range(len(list1)-1):
        if list1[i]<=list1[i+1]:
            count+=1
    if len(list1)==(count+1):
        return True
    else:
        return False
word=[]
for i in (1,4):
    x=input('Enter word:')
    word.append(x)
print(word)
for words in word:
    print(is_abecedarian_fun(words))