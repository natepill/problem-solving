class Solution:
    def romanToInt(self, s: str) -> int:

        hist = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        if s in hist:
            return hist[s]

        count = 0

        for index, char in enumerate(s):
            char_val = hist[char]
            try:
                if hist[s[index+1]] > char_val:
                    count += char_val*-1
                else:
                    count += char_val

            except:
                count += char_val
                continue

        return count
