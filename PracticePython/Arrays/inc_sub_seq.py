class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        for i in range(0, len(nums)-3, 3):

            if self.is_increasing(nums[i:i+3]):
                print(nums[i:i+3])
                return True


        if self.is_increasing(nums[len(nums)-3:len(nums)]):
            # print(nums[i:i+3])
            return True

        else:
            print("end false")
            print(nums[len(nums)-3:len(nums)])
            return False


    def is_increasing(self, nums):
        """ nums is always len 3 """

        if nums[0] < nums[1] and nums[1] < nums[2]:
            return True

        else:
            print(f"is inc False: {nums}")
            return False



            
