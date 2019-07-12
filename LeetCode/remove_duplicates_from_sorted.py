"""
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):

    # init Set
    # iterate through array
        # if num in set
            # continue iterations
        #
    # for index, num in enumerate(nums):
    #     if num in num_set:
    #         nums.pop(index)

    num_set = set()
    index = 0
    while index <= len(nums)-1:
        if nums[index] in num_set:
            nums.pop(index)
            continue

        num_set.add(nums[index])
        index += 1

    return nums



if __name__ == "__main__":
    nums = [0,1,2,2,3,3,0,4,2]
    print(removeDuplicates(nums))
