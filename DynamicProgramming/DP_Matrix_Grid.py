from typing import *

# Problem: Ninja’s Training
# Problem Link: https://takeuforward.org/data-structure/dynamic-programming-ninjas-training-dp-7/
# Problem statement
# Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

# You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

# For Example
# If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.



def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    # Creating a n*4 matrix for dp
    dp = [[-1 for j in range(4)] for i in range(n)]
    # return f(n-1, 3, points)
    return f_mem(n-1, 3, points, dp)

def f_mem(day: int, last: int, points: List[List[int]], dp: List[List[int]]) -> int:

    # Check if the result for this day and last activity is already computed.
    if dp[day][last] != -1:
        return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    maximum = 0
    if day == 0:
        
        for i in range(3):
            if i != last:
                maximum = max(maximum, points[day][i])

        dp[day][last] = maximum
        return dp[day][last]

    # Iterating through all activities for the current day.
    for i in range(3):

        if i != last:
            activity = points[day][i] + f_mem(day-1, i, points, dp)
            maximum = max(maximum, activity)
        
    # Store the maximum points in the DP table and return it.
    dp[day][last] = maximum
    return dp[day][last]

points = [[1,2,5], [3,1,1], [3,3,3]]
n = len(points)
print(f"Ninjas Points Matrix: {points}")
print(f"Maximum points ninja can earn: {ninjaTraining(n, points)}")

    
