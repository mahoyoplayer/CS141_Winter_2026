from sys import stdin, stdout
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
from sys import stdin
stdin = open("../input.txt", "rb")
input = stdin.readline
# DELETE END


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
