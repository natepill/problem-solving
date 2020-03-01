class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        left = 0
        right = len(S)-1

        S = list(S)
        while left < right:

            print(f"left i: {left}")
            print(f"right i: {right}")
            print(f"S: {S}")
            print(f"{S[left]}")
            while not S[left].isalpha() and left < len(S)-1:
                left += 1

            while not S[right].isalpha() and right > 0:
                right -= 1

            if left > right:
                break
            else:
                S[left], S[right] = S[right], S[left]

            left += 1
            right -= 1


        return ''.join(S)
