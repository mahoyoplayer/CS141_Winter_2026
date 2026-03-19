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
arr = [FastIO.getInt() for _ in range(n)]

# There is no need to actually to sort anything.
def pseudo_merge(l, r):
    if r == l + 1:
        return (arr[l], arr[l], 0)
    mid = (l+r) // 2

    a1, b1, c1 = pseudo_merge(l, mid)
    a2, b2, c2 = pseudo_merge(mid, r)

    new_min, new_max = min(a1, a2), max(b1, b2)
    return (new_min, new_max, c1 + c2 + new_max - new_min)


print(pseudo_merge(0, n)[2])