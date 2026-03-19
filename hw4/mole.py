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

# m * m grid, n moles
m, n = FastIO.getInts()
moles = [FastIO.getInts() for _ in range(n)]

# dp[i] = longest path ending at mole i
dp = [1] * n

manhattan = lambda x1, y1, x2, y2: abs(x1-x2) + abs(y1-y2)

for i in range(1, n):
    t1, x1, y1 = moles[i]
    for j in range(i):
        t2, x2, y2 = moles[j]
        if t1 - t2 >= manhattan(x1, y1, x2, y2):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
