'''
815. Bus Routes
Solved
Hard
Topics
conpanies icon
Companies
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
For example, if routes[0] = [1, 5, 7],
this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially),
and you want to go to the bus stop target. You can travel between bus stops by buses only.
Return the least number of buses you must take to travel from source to target.
Return -1 if it is not possible.

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7,
then take the second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

Time Complexity: O(n + m) where n is the number of bus routes and m is the total number of stops across all routes.
Space Complexity: O(n + m) for the graph representation and visited sets.
'''
from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        graph = defaultdict(set)
        print(graph)
        queue = deque([(source, 0)])

        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)  # map stop to bus index

        visited_stops = set()
        visited_buses = set()

        while queue:
            stop, route_len = queue.popleft()

            if stop == target:
                return route_len

            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, route_len + 1))

        return -1  # If we exhaust the queue without finding the target

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(f"expected: 2 actual: {solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)} \n")  # Output: 2
    #print(f"expected: -1 actual: {solution.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12)} \n")  # Output: -1