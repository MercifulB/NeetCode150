class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenLetters = {}

        l = 0
        longest_len = 0

        for r in range(len(s)):
            if s[r] in seenLetters:
                l = max(seenLetters[s[r]] + 1, l)
            seenLetters[s[r]] = r
            longest_len = max(longest_len, r - l + 1)

        return longest_len
        