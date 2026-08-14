import heapq
from typing import List


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # Pop top two elements (largest) using max-heap pop
            s1 = heapq._heappop_max(stones)  # Largest
            s2 = heapq._heappop_max(stones)  # Second largest

            if s1 != s2:
                # Push remaining stone back while maintaining max-heap structure
                heapq._heappush_max(stones, s1 - s2)

        # Return the last remaining stone, or 0 if all stones were destroyed
        return stones[0] if stones else 0