from typing import List, Dict
import heapq


def solve(arr: List[int]) -> int:
    freq: Dict[int, int] = dict()
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    counts: List[int] = list(freq.values())
    heapq.heapify(counts)

    while len(counts) > 1:
        first: int = heapq.heappop(counts)
        second: int = heapq.heappop(counts)

        first -= 1
        second -= 1
        if first > 0:
            heapq.heappush(counts, first)
        if second > 0:
            heapq.heappush(counts, second)
    return counts[0] if len(counts) == 1 else 0


# 1 1 2 2 3 3
# 2 2 2
# 1 1
# 2 1 1
# 2 1
# 1 1
#
if __name__ == "__main__":
    print(solve([1, 3, 2, 3, 1, 2]) == 0)
    print(solve([1, 2, 3]) == 1)
    print(solve([1, 2, 3, 4]) == 0)
