class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []

        sorted_nums = sorted(nums)

        for index, val in enumerate(sorted_nums):
            left = 0
            right = len(sorted_nums)-1

            # may have to add two conditionals for right/left bounds not = curr val
            while left < right or left == index or right == index:

                curr_sum = val + sorted_nums[left] + sorted_nums[right]

                if curr_sum == 0:
                    results.append([val, sorted_nums[left],sorted_nums[right]])
                    break

                elif curr_sum < 0:
                    left += 1

                elif curr_sum > 0:
                    right -= 1


        return results
    
