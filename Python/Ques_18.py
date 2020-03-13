#[7,1,9,2,4,6,8,3] -> [1,9,2,8,3,7,4,6]
def sort_list(num_list):
    num_list.sort()
    print(num_list)
    sort_num_list = []
    i = 0
    j = len(num_list) - 1
    while i < len(num_list) and j > -1 and i < j:
        sort_num_list.append(num_list[i])
        sort_num_list.append(num_list[j])
        i += 1
        j -= 1
    if len(num_list) % 2 != 0:
        sort_num_list.append(num_list[i])
    return sort_num_list


list_inp = [7, 1, 9, 2, 4, 6, 8, 3]
print("Original list : ", list_inp)
print("Sorted list : ", sort_list(list_inp))
