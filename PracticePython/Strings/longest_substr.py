class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        curr_index = 0
        start_index = 0


        while curr_index < len(s):
            seen = set()
            count = 0

            for i in range(start_index, len(s)):
                if s[i] in seen:
                    break
                seen.add(s[i])
                count += 1

            max_len = count if count > max_len else max_len

            start_index += 1
            curr_index += 1


        return max_len
