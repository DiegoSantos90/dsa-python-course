'''
547. Number of Provinces

There are n cities.
Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        if not isConnected:
            return 0

        ROWS, COLS = len(isConnected), len(isConnected[0])
        graph = defaultdict(set)

        for city in range(ROWS):
            for conn in range(COLS):
                if isConnected[city][conn] == 1:
                    graph[city].add(conn)

        visited_cities = set()
        number_of_provences = 0

        def dfs(city):
            visited_cities.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited_cities:
                    dfs(neighbor)

        for city in range(ROWS):
            if city not in visited_cities:
                number_of_provences += 1
                dfs(city)

        return number_of_provences