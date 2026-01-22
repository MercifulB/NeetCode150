class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        total_water = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(height[l], max_l)
                total_water += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                total_water += max_r - height[r]
        
        return total_water
        