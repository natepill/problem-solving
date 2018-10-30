

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersection_list = list()
list1 = set(list1)
list2 = set(list2)



for number in list1:
    for other_num in list2:
        if other_num == number:
            intersection_list.append(other_num)

print(set(intersection_list))
