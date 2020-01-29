class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == None or len(strs)<1:
            return ''

        if strs[0] == '':
            return ''


        prefix = strs[0]
        print(f"prefix: {prefix}")

        for i in range(1, len(strs)):

            # reset prefix for new word
            curr_prefix = ''

            for j in range(0, len(strs[i])):
                try:
                    # compare characters at respective indicies for match
                    if strs[i][j] != prefix[j]:
                        # common prefix end
                        print(f"curr_prefix: {curr_prefix}")
                        break

                    else:
                        # add matched char to current longest substring
                        print(f"new prefix char: {strs[i][j]}")
                        curr_prefix += strs[i][j]
                except:
                    break
            prefix = curr_prefix

        return prefix

                    
