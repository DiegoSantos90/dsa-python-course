'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from collections import defaultdict
from typing import List

#Time Complexity: O(N * K)  # N = length of strs, K = max length of string
#Space Complexity: O(N * K) # Storage needed for all strings in groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(w)

        return list(res.values())

if __name__ == "__main__":
    obj = Solution()
    print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(obj.groupAnagrams([""]))
    print(obj.groupAnagrams(["a"]))

