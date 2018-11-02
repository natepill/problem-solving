
def find_runner_up(arr):

    arr = list(arr)
    arr = set(arr)
    print("after set: {}".format(arr))
    sorted_list = sorted(arr)
    print("after sorted: {}".format(sorted_list))
    sorted_list = (list(sorted_list))
    print("put back into list: {}".format(sorted_list))
    # print(new_array)
    print("runner up: {}".format(sorted_list[-2]))



array = [-10, 0, 10, 10, 10]
find_runner_up(array)
