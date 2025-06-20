'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an array of integers nums and an integer limit,
return the size of the longest non-empty subarray such that the absolute difference
between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

Time Complexity: O(n) where n is the length of the input array nums.
Space Complexity: O(n) for the deques used to maintain the minimum and maximum values in the current window.
'''
from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()  # mono increasing
        max_q = deque()  # mono decreasing
        l = 0
        res = 0

        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res
