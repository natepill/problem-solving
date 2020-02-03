class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

#         Steps to Classical Rotation
#         reverse the first n - k elements

#         reverse the rest of them

#         reverse the entire array
        if len(nums) == 1:
            return nums

        nums[0:len(nums)-k] = reversed(nums[0:len(nums)-k])

        nums[len(nums)-k:] = reversed(nums[len(nums)-k:])

        nums[:] = reversed(nums)

        return nums


#         if len(nums) == 1:
#             return nums

#         if len(nums) == 2:
#             # print("HERE")
#             if k%2 == 1:
#                 nums[0], nums[1] = nums[1], nums[0]
#                 return nums
#             else:
#                 return nums

#         nums[:] = reversed(nums)

#         nums[0:k] = reversed(nums[0:k])

#         nums[k:len(nums)] = reversed(nums[k:len(nums)])

#         return nums

#         if nums is None or len(nums)==1:
#             return nums
#         # iterate over backwards range of k indicies
#         og_k = k
#         k -=1
#         # iterate over backwards range of k indicies
#         for i in range(-1, -k-2, -1):

#             # swap each val at backwards indicie at k indicie
#             nums[k], nums[i] = nums[i], nums[k]

#             k -= 1

#         for i in range(og_k, len(nums)-og_k):
#             print(i)
#             nums.insert(len(nums), nums.pop(og_k))
