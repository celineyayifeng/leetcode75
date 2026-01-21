You are working as a data engineer, and you need to analyze and optimize the execution windows of multiple data pipelines. 
Each pipeline has a start and end time. When pipelines have overlapping execution times, you want to merge them to: 
    1. Understand the actual time ranges when pipelines are running 
    2. Optimize resource allocation 
    3. Identify potential pipeline consolidation opportunities
    
Write a function that: 
    1. Takes a list of time intervals (start_time, end_time) 
    2. Merges any overlapping intervals 
    3. Returns the consolidated time ranges in sorted order 
    
    Input: [(1, 4), (2, 3), (3, 6), (5, 7), (6, 8)] 
    Output: [(1, 8)] 

def merge_intervals(intervals): 
    # sort interval by start time
    sort_intervals = sorted(intervals, key = lambda x: x[0]) 
    # initialize result with the first interval 
    merged = [sorted_intervals[0]] # Step 1: Start with [(1,4)]
    # process each interval 
    for current_start, current_end in sorted_intervals[1: ]: # Go to the next interval 
        last_start, last_end = merged[-1] # gives the last interval in the result list
        # check if current interval overlaps with the last merged interval 
        if current_start <= last_end: # 2 ≤ 4 (overlaps) 
            merged[-1] = (last_start, max(last_end, current_end)) # merge to (1, max(4,3)) = (1,4)
        else:
            # no overlap: add as a new interval
            merged.append((current_start, current_end))
    return merged 


Sorted intervals: [(1,4), (2,3), (3,6), (5,7), (6,8)]

Step 1: Start with [(1,4)]

Step 2: (2,3) → 2 ≤ 4 (overlaps) → merge to (1, max(4,3)) = (1,4)
        Result: [(1,4)]

Step 3: (3,6) → 3 ≤ 4 (overlaps) → merge to (1, max(4,6)) = (1,6)
        Result: [(1,6)]

Step 4: (5,7) → 5 ≤ 6 (overlaps) → merge to (1, max(6,7)) = (1,7)
        Result: [(1,7)]

Step 5: (6,8) → 6 ≤ 7 (overlaps) → merge to (1, max(7,8)) = (1,8)
        Result: [(1,8)]
    
