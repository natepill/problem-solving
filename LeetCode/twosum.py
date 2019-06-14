class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add_possibilities = {}

        for index, number in enumerate(nums):
            added_number = target-number
            if added_number in add_possibilities:
                return [add_possibilities[added_number], index]
            else:
                add_possibilities[number] = index

        return None
        
