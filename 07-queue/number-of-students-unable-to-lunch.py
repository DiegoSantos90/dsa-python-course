from collections import defaultdict
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = defaultdict()
        # cnt = Counter(students)

        for stu in students:
            cnt[stu] = cnt.get(stu, 0) + 1

        for s in sandwiches:
            if s in cnt and cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res

        return res
