import string

num = string.digits
# print(num)


def phone_number(s):
    phone_num = []
    for i in s:
        if i in num:
            phone_num.append(i)
    # print(phone_num)
    phone_num.insert(3, '-')
    phone_num.insert(7, '-')
    # print(phone_num)

    phone_num2 = ''
    for i in phone_num:
        phone_num2 += i
    print(phone_num2)

    india = ['in', 'ind', 'india']
    usa = ['us', 'usa']
    for i in india:
        if i in s:
            phone_num2 = '+91 '+phone_num2
            break
    print(phone_num2)

    for u in usa:
        if u in s:
            phone_num2 = '+1 '+phone_num2
            break
    print(phone_num2)


s = 'lskdfng706dfg618fgfgiubfbh5899'
phone_number(s)
