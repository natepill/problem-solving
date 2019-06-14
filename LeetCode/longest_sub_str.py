# TODO:
'''
    Instead of nested for loops, let's refactor to implement an index_counter and then
    reset the index_counter when we "see" a char that we've seen before
'''

# NOTE: I'm keeping the non working solution as a reminder of when to use nested
# for loops vs index counters and accessing values in structures by their index

# def longest_substr(string):
#     ''' Return the LENGTH of the longest substring in the string '''
#
#     seen = set()
#     curr_counter = 0 # current length of iterated substring
#     longest = 0 # length of longest seen substring
#
#     #loop over input string, tracking the starting character of each substring
#     for start_char in string:
#
#         # iterating over each substring
#         for char in string:
#             if char in seen:
#                 # About to start new substring with no previously seen characters
#                 seen = set()
#                 longest = curr_counter if curr_counter > longest else longest
#                 break
#
#             else:
#                 curr_counter += 1
#                 seen.add(char)
#
#     return longest

# "abcabcbb"


def longest_substr(string):
    ''' Return the LENGTH of the longest substring in the string '''

    seen = set()

    curr_counter = 0 # current length of iterated substring
    longest = 0 # length of longest seen substring

    substr_index = 0 # Tracking where we are in the string during iteration
    index_curr = 0 # Where we are in the string
    last_index = len(string)

    # Stop iterating when we've seen all possibile substrings in the string
    while index_curr < last_index:
        curr_char = string[index_curr]
        print("current char: ", curr_char)
        # print(curr_char)

        # End of current substring
        if curr_char in seen:
            seen = set()
            substr_index += 1
            index_curr = substr_index
            curr_counter = 0

        # Continue substring
        else:
            print("else")
            index_curr += 1
            curr_counter += 1
            seen.add(curr_char)

    return max(curr_counter, longest)




if __name__ == "__main__":

    # Test inputs
    Input = "dvdf" # expect 3

    print(longest_substr(Input))
