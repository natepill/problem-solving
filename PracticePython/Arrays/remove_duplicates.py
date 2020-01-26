class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # method 1: iterate over array, add seen numbers to a set, if nums have been seen
        # don't increment length_counter

        # method 2: iterate over indicies and pop repeated vals and inc length counter


        # edge case for short arrays
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)


        i = 0

        # loop over index range

            # wrap in try-except for out of bounds
                # check left, check right for dup


        while i < len(nums):

            try:
                if nums[i] == nums[i+1]:
                    nums.pop(i)
                    i -= 1
            except:
                break

            i += 1

            print(i)
        return len(nums)
            
