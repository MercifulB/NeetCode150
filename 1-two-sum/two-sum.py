class Solution:
    # O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 result = [i, j]
    #                 return result
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for i, num in enumerate(nums): # enumerate create tuple of (index, value)
            complement = target - num
            if complement in seenNums:
                return [seenNums[complement], i]
            
            seenNums[num] = i

        
        