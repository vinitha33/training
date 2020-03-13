# Given a list of words. Sort the list on the basis of the 2nd letters of each word contained in the list

list1 = ['weap', 'wdqm', 'wamn', 'wzkl']
print("Original list:", list1)

list2 = sorted(list1, key=lambda x: x[1])
print("Sorted list:", list2)
