class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort_intervals = sorted(intervals, key=lambda x:x[1])

        output = 0
        prev_end = float('-inf')

        for start, end in sort_intervals:
            if start >= prev_end:
                prev_end = end
            else:
                output += 1

        return output
