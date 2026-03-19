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



n, k = FastIO.getInts()
prices = [FastIO.getInt() for _ in range(k)]
s = FastIO.getStr()

dp = [[0] * n for _ in range(n)]
    
base = ord("a")

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            l = dp[i][j-1] + prices[ord(s[j]) - base]
            r = dp[i+1][j] + prices[ord(s[i]) - base]
            dp[i][j] = min(l, r)
            
print(dp[0][-1])
