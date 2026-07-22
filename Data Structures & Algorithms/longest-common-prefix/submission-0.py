class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        shortestWord = len(min(strs, key=len))
        result = []  # Use a list instead of a string

        for i in range(shortestWord):
            char = strs[0][i]
            if all(string[i] == char for string in strs):
                result.append(char)
            else:
                break

        return "".join(result)  # O(M) time single build