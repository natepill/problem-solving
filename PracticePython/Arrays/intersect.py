def intersect(nums1, nums2):

    # denote lists as smaller or larger
    sm_arr, lg_arr = (nums1, nums2) if len(nums1)<len(nums2) else (nums2, nums1)

    # sm_arr = nums2
    # lg_arr = nums1

    # make hist of lg_arr
    # iterate over sm_arr, if not in lg_arr hist --> pop it, if it is --> append key
    #   a value number of times to end of sm_array
    # return sm_arr

    hist = {} # O(n) space
    intersect = []

    # O(m) time
    for val in lg_arr:
        if val in hist:
            hist[val] +=1
        else:
            hist[val] = 1

    print(hist)

    for i,val in enumerate(sm_arr):
        # print(i)
        if val in hist:
            for _ in range(0,hist[val]-1):
                intersect.append(val)

            del hist[val]

    return intersect


if __name__ == "__main__":
    arr1 = [1,2,2,1]
    arr2 = [2,2]

    print(intersect(arr1, arr2))
