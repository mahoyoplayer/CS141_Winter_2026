from sys import stdout, stdin
import io, os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class FastIO:
  @staticmethod
  def getInt() -> int:
      return int(input())

  @staticmethod
  def getInts() -> list[int]:
      return(list(map(int,input().split())))

  @staticmethod
  def getStr() -> str:
      return input().strip()

  @staticmethod
  def getStrs() -> list[str]:
      return input().strip().split()

# DELETE START
stdin = open("../input.txt", "r")
input = stdin.readline
# DELETE END

n, coins = FastIO.getInt(), FastIO.getInts()
total = sum(coins)
dp = [False] * (total + 1)
dp[0] = True
for coin in coins:
    for i in range(total, coin-1, -1):
        dp[i] = dp[i] or dp[i - coin]
 
 
print(dp.count(True) - 1)
print(' '.join(str(x) for x in range(1, total + 1) if dp[x]))