"""
Given an array nums and a value val, remove all instances of that value
in-place and return the new length.

Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what
 you leave beyond the new length.
"""

def removeElement(nums, val):

    # length = 0
    # for index, num in enumerate(nums):
        # print(num)
        # if num == val:
        #     nums.pop(index)
        # length += 1
    # return nums

    index = 0
    while index <= len(nums)-1:
        if nums[index] == val:
            print(nums[index])
            nums.pop(index)
            index -= 1

        index += 1

    return nums
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(nums, val))
