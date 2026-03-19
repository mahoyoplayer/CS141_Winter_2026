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

"""
Problem - 
Find the longest decreasing path in a matrix.
Can move left, right, up, or down.

Solution - 
DP + DFS
O(r*c)
"""
r, c = FastIO.getInts()
h = [FastIO.getInts() for _ in range(r)]

dp = [[-1] * c for _ in range(r)]
valid = lambda i, j: 0 <= i < r and 0 <= j < c
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    longest_path = 1
    for deltaY, deltaX in dirs:
        new_i, new_j = i + deltaY, j + deltaX
        if not valid(new_i, new_j) or h[i][j] <= h[new_i][new_j]:
            continue
        longest_path = max(longest_path, 1 + dfs(new_i, new_j))
    dp[i][j] = longest_path
    return longest_path

longest = 0
for i in range(r):
    for j in range(c):
        if dp[i][j] == -1:
            dfs(i, j)
        longest = max(longest, dp[i][j])
print(longest)
