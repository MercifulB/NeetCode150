class Solution:
   # def containsDuplicate(self, nums: List[int]) -> bool:
   #     seenNums = []
   #     for i in range(len(nums)):
   #         if nums[i] in seenNums:
   #             return True
   #         seenNums.append(nums[i])
   #     return False
  
   def containsDuplicate(self, nums: List[int]) -> bool:
       seenNums = {}
       for i, num in enumerate(nums):
           if num in seenNums:
               return True
           seenNums[num] = i
       return False
