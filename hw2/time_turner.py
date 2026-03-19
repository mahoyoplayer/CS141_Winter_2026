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
classes = [FastIO.getInts() for _ in range(n)]
# Sort by ending time
classes.sort(key = lambda x: x[1])

took, time1, time2 = 0, -1, -1
for start, end in classes:
    take1, take2 = start > time1, start > time2
    if take1 and take2:
        if time1 > time2:
            take2 = False
        else:
            take1 = False
    if take1:
        time1 = end
        took += 1
    elif take2:
        time2 = end
        took += 1

print(took)
