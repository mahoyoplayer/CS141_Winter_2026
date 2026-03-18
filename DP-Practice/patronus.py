import sys
input = sys.stdin.buffer.readline

class FastIO:
    @staticmethod
    def getInt() -> int:
      return int(input())

    @staticmethod
    def getInts():
        return (list(map(int,input().split())))

    @staticmethod
    def getStr() -> str:
        return input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
      return input().decode().split()

# DELETE START
stdin = open("../input.txt", "rb")
input = stdin.readline
# DELETE END

n, happy = FastIO.getInt(), FastIO.getInts()

dp = happy[:]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if happy[j] < happy[i]:
            dp[i] = max(dp[i], dp[j] + happy[i])

print(max(dp))