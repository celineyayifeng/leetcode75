/***
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
***/
