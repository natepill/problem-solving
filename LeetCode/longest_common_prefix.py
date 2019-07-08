def longestCommonPrefix(strs: List[str]) -> str:
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
    prefix = list()
    for word in strs:
        curr_prefix = list()

        for index in range(0, len(word)-1):

            if word[index] == prefix[index]:
                curr_prefix.append(word[index])
            else:
                break




if __name__ == "__main__":


    # input =
    print(longestCommonPrefix(input))

# Input: ["flower","flow","flight"]
# Output: "fl"
