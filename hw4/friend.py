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

# This problem is basically Edit Distance from Leet
n = FastIO.getInt()
s1, s2 = [FastIO.getStr() for _ in range(2)]

dp = [[0] * (n+1) for _ in range(n+1)]

# dp[n1][n2] = cost to make s1[:n1+1] == s2[:n2+1]
for i in range(1, n+1):
    dp[0][i] = i
    dp[i][0] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            rem = dp[i-1][j] + 1
            ins = dp[i][j-1] + 1
            sub = dp[i-1][j-1] + 1
            dp[i][j] = min(ins, rem, sub)

print(dp[n][n])

