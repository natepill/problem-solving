def longestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """

    prefix = strs[0]

    for word in strs:

        curr_prefix = ''

        print("word:", word)

        for index in range(0, len(word)):

            # if len(prefix)
            print("index:", index)
            print("word[index]:", word[index])
            # print("prefix[index]:", prefix[index])
            print("curr_prefix:", curr_prefix)
            # ["aca","cba"]
            try:
                if word[index] == prefix[index]:
                    curr_prefix += word[index]
                else:
                    break
            except:
                break

            print("curr_prefix:", curr_prefix)

        if len(curr_prefix) <= len(prefix):
            prefix = curr_prefix


    return prefix


if __name__ == "__main__":


    # input = ["rfnlower","efwlow","wfqlight","qfwlip"]
    # input = ["al", 'alp', 'alpha']
    input = ["aca","cba"]
    print(longestCommonPrefix(input))

    # input: ["flower","flow","flight"]
    # Output: "fl"
