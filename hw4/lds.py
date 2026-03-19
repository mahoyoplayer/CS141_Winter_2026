import sys

class FastIO:
    import os
    # Try to use local input file if exists
    if os.path.exists(input_file := os.path.splitext(__file__)[0] + ".txt"):
        sys.stdin = open(input_file, "r")
    input = sys.stdin.buffer.readline

    @staticmethod
    def getInt() -> int:
        return int(FastIO.input())

    @staticmethod
    def getInts():
        return list(map(int, FastIO.input().split()))

    @staticmethod
    def getFloat() -> float:
        return float(FastIO.input())

    @staticmethod
    def getFloats() -> list[float]:
        return list(map(float, FastIO.input().split()))

    @staticmethod
    def getStr() -> str:
        return FastIO.input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
        return FastIO.input().decode().split()

n = FastIO.getInt()
nums = FastIO.getInts()

# DP, O(n^2) time
def dp_sol():
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

import bisect
# O(n log n)
# Idea is to convert this to a LIS problem
def greedy_sol():
    curr = []
    for num in nums:
        num = -num
        if not curr or num > curr[-1]:
            curr.append(num)
        else:
            # Try to improve
            idx = bisect.bisect_left(curr, num)
            curr[idx] = num
    return len(curr)

#print(dp_sol())
print(greedy_sol())
