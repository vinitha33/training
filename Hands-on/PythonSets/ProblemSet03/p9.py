def is_sorted(list1):
    if list1 == sorted(list1):
        return True
    else:
        return False


def is_sorted_fun(list1):
    count = 0
    for i in range(len(list1) - 1):
        if list1[i] <= list1[i + 1]:
            count += 1
    if len(list1) == (count + 1):
        return True
    else:
        return False


list1 = []
for i in range(1, 6):
    num = input("Enter value:")
    list1.append(num)
print(list1)
print(is_sorted(list1))
print(is_sorted_fun(list1))