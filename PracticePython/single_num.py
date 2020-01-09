"""

    I completed this problem with dictionary, if key surpasses 1, then remove key
    Need to learn bitwise operators to unlock the O(1) memory --> See second function

"""



def singleNumber(nums) -> int:

    seen = dict()

    for num in nums:
        if num in seen:
            del seen[num]
        else:
            seen[num] = 1

    for key in seen:
        return key

def singleNumber(nums) -> int:
    temp = 0
    for each in nums:
        temp ^= each
    return temp


if __name__ == "__main__":

    arr = [4,1,2,1,2]
    print(singleNumber(arr))
