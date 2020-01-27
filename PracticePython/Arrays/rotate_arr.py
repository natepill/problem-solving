def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    og_k = k
    k -=1
    # iterate over backwards range of k indicies
    for i in range(-1, -k-2, -1):

        # swap each val at backwards indicie at k indicie
        nums[k], nums[i] = nums[i], nums[k]

        k -= 1

    for i in range(og_k, len(nums)-og_k):
        print(i)
        nums.insert(len(nums), nums.pop(og_k))


# def rotate(self, nums: List[int], k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     k %= len(nums)
#     nums.reverse()
#
#     i = 0
#     j = k-1
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
#
#     nums[k:] = reversed(nums[k:])







if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    rotate(arr, 3)
    print(arr)
    #
    # for i in range(-1, -3-1, -1):
    #     print(i)
