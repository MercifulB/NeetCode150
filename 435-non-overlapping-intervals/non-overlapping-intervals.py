class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda i: i[0])
        countOverlap = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            
            if start >= prevEnd:
                prevEnd = end
            else:
                countOverlap += 1
                prevEnd = min(prevEnd, end)

        return countOverlap
        