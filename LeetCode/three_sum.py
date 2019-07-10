
def threeSum(nums):

    result = list()

    for index, num in enumerate(nums):
        zero_target_sum = num*-1

        complement_pair = set()

        for index2, num2 in enumerate(nums):

            if index2 == index:
                continue

            if num2 + zero_target_sum in complement_pair:
                result.append([num, num2, num2 + zero_target_sum])
                # complement_pair[zero_target_sum]

            complement_pair.add(num2)

    return result

if __name__ == "__main__":
    input = [-1, 0, 1, 2, -1, -4]
    print(threeSum(input))
