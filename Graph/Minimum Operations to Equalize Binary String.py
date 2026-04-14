from collections import deque
from sortedcontainers import SortedList
import math

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero_count = s.count("0")

        dist = [math.inf] * (n + 1)

        even = SortedList(range(0, n + 1, 2))
        odd = SortedList(range(1, n + 1, 2))

        queue = deque([zero_count])
        dist[zero_count] = 0

        (even if zero_count % 2 == 0 else odd).remove(zero_count)

        while queue:
            curr = queue.popleft()

            left = max(k - n + curr, 0)
            right = min(curr, k)

            start = curr + k - 2 * right
            end = curr + k - 2 * left

            target_set = even if start % 2 == 0 else odd

            i = target_set.bisect_left(start)

            while i < len(target_set) and target_set[i] <= end:
                nxt = target_set[i]

                dist[nxt] = dist[curr] + 1
                queue.append(nxt)

                target_set.pop(i) 

        return -1 if dist[0] == math.inf else dist[0]