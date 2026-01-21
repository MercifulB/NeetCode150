class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_count = 1
        current_count = 1

        nums.sort()

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            next_diff = nums[i + 1] - nums[i]
            
            if next_diff == 1:
                current_count += 1
                longest_count = max(longest_count, current_count)
            
            elif next_diff == 0:
                continue

            else:
                current_count = 1
            
        return longest_count
