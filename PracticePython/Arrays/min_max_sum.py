def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    print(sorted_arr[5:0:-1])
    print(sorted_arr[0:4:1])
    addMax = sum(sorted_arr[:1-1])
    addMin = sum(sorted_arr[::])
    # print(addMax)
    # print(addMin)
    return '{} {}'.format(addMin, addMax)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    # arr = [7, 69, 2, 221, 8974]
    print(miniMaxSum(arr))
