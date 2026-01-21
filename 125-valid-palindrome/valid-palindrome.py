class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1

        while first < last:
            while first < last and not self.alphaNum(s[first]):
                first += 1
            
            while last > first and not self.alphaNum(s[last]):
                last -= 1

            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
                