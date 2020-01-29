class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # if num > 9:
            # subtract 1 from num
            # if at start then
                #insert 1 at start of array

            # add 1 to next element

        # else
            # return nums



       # add 1 to last element
        digits[-1] += 1
        print(digits[-1])
        # iterate over list backwards
        for i in range(len(digits)-1,-1, -1):

            # Account for carry over
            print(i)
            print(digits[i])

            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    print(digits)

                else:
                    digits[i-1] += 1

            else:
                # all digits are less than 10. 1 has been added to end
                return digits

        return digits

            
