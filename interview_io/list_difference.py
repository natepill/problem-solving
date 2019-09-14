# https://www.youtube.com/watch?v=cdCeU8DJvPM


def reverse_string(string):
    """ Reverse input string  """

    reversed_string = ''

    for char in string:
        reversed_string = char + reversed_string

    return reversed_string


sample_string = 'apple'
print(reverse_string(sample_string))


def find_missing(arr1, arr2):
    """ Return missing value from either array """




sample_arr = [1,3,2,6,5]
sample_arr2 = [2,3,1,5]
print(find_missing(sample_arr, sample_arr2)) # Should return 6
