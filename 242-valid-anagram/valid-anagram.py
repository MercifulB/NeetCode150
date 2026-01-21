class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
           return False
       freqMapS = Counter(s)
       freqMapT = Counter(t)
       for char, count in freqMapS.items():
           if count != freqMapT[char]:
               return False
       return True
      
