class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for word in strs:

            if tuple(sorted(word)) in seen:
                seen[tuple(sorted(word))].append(word)
            else:
                seen[tuple(sorted(word))] = [word]

        return seen.values()
            
