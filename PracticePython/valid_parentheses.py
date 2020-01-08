
"""
    This actually is the wrong answer for the LeetCode question, but is actually a Solution
    to a harder problem. Their definition of valid parentheses was very basic while they were
    just looking at the immidiete bracket right next to a given char.

    My solution returns True or False for actual valid parentheses phrases. See below:

    Input: "([)]"
    Output: true

    However, LeetCode would define this as false.

    Major Takeaway: Make sure to read, understand, and ask for test cases before designing a solution
"""


from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        opening_chars = {'(':')', '{':'}', '[':']'}
        closing_chars = {')':'(', '}':'{', ']':'['}
        queue = deque()

        for char in s:
            if char in opening_chars:
              queue.append(char)
            else:
                # print(char)
                # print(queue)
                # if opening bracket in front of queue doesnt =
                if queue[0] != closing_chars[char]:
                    return False
                else:
                    if len(queue) > 0:
                        queue.popleft()

        if len(queue) > 0:
            return False
        else:
            return True

        # Create Queue --> only opening?
        # create set of opening and closing chars

        # Traverse the string
            # add opening characters to the queue

            # deque closing characters
            # if dequed closing chars do not close current char
                # return False


        # if anything left in queue then return false
        # else return True
