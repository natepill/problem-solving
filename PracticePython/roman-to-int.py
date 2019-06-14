def romanToInt(s):

    hist = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    if s in hist:
        return hist[s]

    count = 0

    for index, char in enumerate(s):
        print('{},{}'.format(index, char))
        char_val = hist[char]
        try:
            if hist[s[index+1]] > char_val:
                print("here")
                count -= char_val
            else:
                count += char_val
        except:
            print("Except")
            count += char_val
            continue

    return count


print(romanToInt('IV'))
# print(romanToInt('III'))








    # class Solution:
    # def romanToInt(self, s: str) -> int:
    #
    #     hist = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #
    #     if s in hist:
    #         return hist[s]
    #
    #     count = 0
    #
    #     for index, char in enumerate(s):
    #         char_val = hist[char]
    #         try:
    #             if hist[s[index+1]] > char_val:
    #                 count -= char_val
    #         except:
    #             count += char_val
    #
    #     return count
    #
