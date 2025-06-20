'''
269. Alien Dictionary

There is a new alien language that uses the English alphabet.
However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary.
Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot
correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules.
If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

Time Complexity: O(N + E)  # N = number of characters, E = number of edges
Space Complexity: O(N + E)  # Space for the adjacency list and the visited set
'''
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    print(f"expected=wertf , actual={sol.alienOrder(["wrt","wrf","er","ett","rftt"])} \n")
    print(f"expected=zx , actual={sol.alienOrder(["z","x"])} \n")
    print(f"expected=zx , actual={sol.alienOrder(["z","x","z"])} \n")

