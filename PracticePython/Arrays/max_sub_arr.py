""" https://www.youtube.com/watch?v=86CQq3pKSUw """
def maxSubArray(nums) -> int:

    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    curr_max = nums[0]

    for i in range(0, len(nums)):

        curr_max = max(nums[i], curr_max+nums[i])
        print(nums[i])
        print(curr_max+nums[i])
        print(curr_max)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


if __name__ == "__main__":
    # arr = [-2, -3, 4, -1, -2, 1, 5, -1] # --> 7
    arr = [-2, 1]
    print(maxSubArray(arr))
