'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?

Time Complexity: O(n)  # Single pass through both strings
Space Complexity: O(1)  # Constant space for character counts (assuming a fixed alphabet size)
'''
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_s = {}
        char_t = {}

        for i in range(len(s)):
            char_s[s[i]] = char_s.get(s, 0) + 1
            char_t[t[i]] = char_t.get(t, 0) + 1

        return True if char_s == char_t else False

        #return Counter(s) == Counter(t)

if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))
    print(obj.isAnagram("rat", "car"))
