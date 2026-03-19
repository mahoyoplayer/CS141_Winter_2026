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

n, m = FastIO.getInts()
children = [[] for _ in range(n)]

# Set up parents
for child in range(1, n):
    parent = FastIO.getInt()
    children[parent].append(child)

# Set up traitors
traitors = set()
for _ in range(m):
    traitors.add(FastIO.getInt())

dp = [-1] * n

def dfs(person):
    if dp[person] != -1:
        return dp[person]
    
    res = 1
    if person in traitors:
        res = 0
    else:
        for child in children[person]:
            res += dfs(child)
    dp[person] = res
    return res

for i in range(n):
    if dp[i] == -1:
        dfs(i)

print(max(dp))
