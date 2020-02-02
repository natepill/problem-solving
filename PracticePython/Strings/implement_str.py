class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        if needle == '':
            return 0

        if haystack == '':
            return -1

        # enumerate over haystack
        for i, char in enumerate(haystack):

            # find match with start of needle at curr index in haystack
            if char == needle[0]:

                try:
                    # compare needle to slice of haystack from curr index to len of needle
                    if needle == haystack[i: i+len(needle)]:

                        # found needle, return start
                        return i

                except:
                    # needle search out of bounds, so no longer possible to find needle
                    return -1

        # needle not found
        return -1






        
