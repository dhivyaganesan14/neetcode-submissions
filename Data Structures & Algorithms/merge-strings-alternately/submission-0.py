class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = ''
        i = 0
        total_length = len(word1) + len(word2)
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                final_str += word1[i]
            if i < len(word2):
                final_str += word2[i]
            i += 1
        return final_str

# Time Complexity = O(n+m)
# Space Complexity = O(n+m)