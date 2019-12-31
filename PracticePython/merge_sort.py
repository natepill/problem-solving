def merge_sort(arr):
    # print("arr:", arr)

    # base case
    if len(arr) <= 1:
        return arr

    # recursive call on two halves
    index_half = len(arr)//2

    left_arr = arr[0:index_half]
    right_arr = arr[index_half:]

    # print("left_arr:", left_arr)
    # print("right_arr:", right_arr)

    merge_sort(left_arr)
    merge_sort(right_arr)
    # print(left_arr)
    # print(right_arr)

    # print(merged_left, merged_right)
    # print("Merged:", merge(left_arr, right_arr))
    # print(f'{left_arr} --- {right_arr}')
    merged_items = merge(left_arr, right_arr)
    # copies the sorted part each time
    arr[:] = merged_items



# def merge(arr1, arr2):
#
#     print("arr1:", arr1)
#     print("arr2:", arr2)
#     # check if lists are empty
#     if not arr1 and not arr2:
#         return []
#
#     sorted_arr = []
#     sm_index = 0
#     lg_index = 0
#     # print("arr1:", arr1)
#     # print("arr2:", arr2)
#
#     sm_arr, lg_arr = (arr1, arr2) if len(arr1) < len(arr2) else (arr2, arr1)
#
#     print("sm arr:", sm_arr)
#     print("lg arr:", lg_arr)
#
#     while sm_index < len(sm_arr)-1:
#         if sm_arr[sm_index] <= lg_arr[lg_index]:
#             sorted_arr.append(sm_arr[sm_index])
#             sm_index += 1
#
#         else:
#             sorted_arr.append(lg_arr[lg_index])
#             lg_index += 1
#
#
#     # sorted_arr.extend(sm_arr[sm_index:])
#     # sorted_arr.extend(lg_arr[lg_index:])
#     while lg_index < len(lg_arr)-1:
#         sorted_arr.append(lg_arr[lg_index])
#
#     print("sorted_arr:", sorted_arr)
#     return sorted_arr


def merge(arr1, arr2):

    # check if lists are empty
    if not arr1 and not arr2:
        return []

    index1, index2 = 0,0
    merged_list = []

    while index1<len(arr1) and index2<len(arr2):
        if arr1[index1] <= arr2[index2]:
            merged_list.append(arr1[index1])
            index1 += 1
        else:
            merged_list.append(arr1[index2])
            index2 += 1

    if index1 > len(arr1)-1:
        while index1 < len(arr1):
            merged_list.append(arr1[index1])
            index1+=1

    elif index2 > len(arr2)-1:
        while index2 < len(arr2):
            merged_list.append(arr2[index2])
            index2+=1


    return merged_list



#
# def merge_sort(items):
#     """
#     Sort given items by splitting list into two approximately equal halves,
#     sorting each recursively, and merging results into a list in sorted order.
#     Running time: O(nlogn) in all cases, as we need to split the array
#     approximately two equal parts in a O(logn) time and merge them back in O(n)
#     run time. so overall O(nlogn)
#     Memory usage: O(nlogn) for recursive stack. (it could be reduced down to
#     O(n)).
#
#     Args:
#         items(list): unsorted list of elements
#
#     Returns:
#         merged_list(list): unsorted list of elements
#     """
#     # base case if there is only 1 or 0 item in the list return itself
#     # since it is already sorted
#     if len(items) <= 1:
#         return items
#
#     mid = len(items) // 2
#     items_1 = items[0:mid]
#     items_2 = items[mid:]
#
#     merge_sort(items_1)
#     merge_sort(items_2)
#     # print(f"items_1: {items_1}, items_2: {items_2}")
#
#     merged_items = merge(items_1, items_2)
#     # copies the sorted part each time
#     items[:] = merged_items
#
#
#
# def merge(items_1, items_2):
#     """
#     Merge given lists of items, each assumed to already be in sorted order,
#     and return a new list containing all items in sorted order.
#     Running time: O(n+m) where n and m are lengths of two sorted lists
#     Memory usage: O(n+m) where n and m are lengths of two sorted lists,
#     Runnning and memory time is the same for all cases, because we always copy
#     all elements from both lists to new merged list.
#     Args:
#         items_1(list): sorted list of elements
#         items_2(list): sorted list of elements
#     Returns:
#         merged_list(list): merged list of the two sorted lists
#     """
#     # check if lists are empty
#     if not items_1 and not items_2:
#         return []
#
#     # used to merge two sorted lists together
#     merged_list = []
#     index1, index2 = 0, 0
#
#     # iterate until one or both list are done
#     while (index1 < len(items_1)) and (index2 < len(items_2)):
#         # print(f"i: {index1}, j: {index2}")
#         if items_1[index1] <= items_2[index2]:
#             merged_list.append(items_1[index1])
#             index1 += 1
#         else:
#             merged_list.append(items_2[index2])
#             index2 += 1
#
#     # check if there are still elements in items_1
#     if index1 <= len(items_1)-1:
#         # copy the rest of the elements from array items_1 to merged_list
#         while index1 < len(items_1):
#             merged_list.append(items_1[index1])
#             index1 += 1
#
#     # check if there are still elements in items_2
#     elif index2 <= len(items_2)-1:
#         # copy the rest of the elements from array items_2 to merged_list
#         while index2 < len(items_2):
#             merged_list.append(items_2[index2])
#             index2 += 1
#
#     return merged_list

if __name__ == "__main__":
    #
    # arr = sorted([9,6,2,5,1,6,8,4,11])
    # arr2 = sorted([2,8,2,7,4,3])
    #
    # print(merge(arr, arr2))

    arr1 = [2,5,1,6,8,4,11]
    merge_sort(arr1)
    print(arr1)


    # print(merge_sort(arr1))
