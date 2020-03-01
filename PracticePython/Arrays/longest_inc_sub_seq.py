class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        # window_end = 1
        global_max = 0
        curr_max = 1
        i = 1

        while i < len(nums):

            if nums[i] > nums[i-1]:
                curr_max += 1

            else:
                curr_max = 1

            global_max = curr_max if curr_max > global_max else global_max

            i += 1


        return global_max


#         while index < len(nums)-1:

#             if nums[window_end] > nums[window_end-1]:
#                 window_end += 1
#                 curr_max += 1

#             else:
#                 global_max = curr_max if curr_max > global_max else global_max


        
