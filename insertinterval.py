class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        sort_intervals = sorted(intervals, key=lambda x: x[0])

        merged = [sort_intervals[0]]

        for current_start, current_end in sort_intervals[1: ]:
            last_start, last_end = merged[-1]
            if last_end >= current_start:
                merged[-1] = ((last_start, max(current_end, last_end)))
            else:
                merged.append((current_start, current_end))
        return merged
        
