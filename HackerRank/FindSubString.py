"""
Find the amount of times the sub_string occurs in the original string
"""

"""
Refactor code to increment the index in range of the length of the original string because
the index(obj) function is resetting the index at an earlier occurence of a letter in
the sub_string to where the index is supposed to be at.
"""

# def count_substring(word, sub_string):
#     counter = 0
#     for letter in word:
#         index = word.index(letter)
#         if sub_string in word[index:(index+len(sub_string))]:
#             counter += 1
#
#     return counter


def count_substring(word, sub_string):

    counter = 0
    index = 0
    for letter in range(len(word)):
        if sub_string in word[index:index+len(sub_string)]:
            counter += 1
        index += 1

    return counter






if __name__ == "__main__":
    print(count_substring("ABCDCDC", "CDC"))
    # print(count_substring("abcdcdc", "cdc"))
    # print(count_substring("abcdcdcdcdcd", "cd"))
