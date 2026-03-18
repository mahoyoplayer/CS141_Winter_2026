import sys
import os

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

#region
base = os.path.splitext(__file__)[0]
input_file = base + ".txt"
if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")
input = sys.stdin.buffer.readline
#endregion

n, m = FastIO.getInts()
 
if n == 0:
    sys.stdout.write("0")
    sys.exit()
 
edges = [0] * m
for i in range(m):
    edges[i] = FastIO.getInts()
# Sort edges by cost
edges.sort(key = lambda x: x[2])
 
labels = list(range(n))

# Number of edges to get to parent
rank = [0] * n

def findParent(v):
    if labels[v] == v:
        return v
    labels[v] = findParent(labels[v])
    return labels[v]
   
def union(u_p, v_p):
    # Always move lesser into greater
    if rank[u_p] < rank[v_p]:
        labels[u_p] = v_p
    elif rank[v_p] < rank[u_p]:
        labels[v_p] = u_p
    else:
        labels[u_p] = v_p
        rank[v_p] += 1
        

worst = 0
used = 0
for u, v, cost in edges:
    u_p, v_p = findParent(u), findParent(v)
    if u_p == v_p:continue
    """
    for i in range(n):
        if i == loc1: 
            continue
        if labels[i] == labels[loc1]:
            labels[i] = labels[loc2]
    labels[loc1] = labels[loc2]
    """
    union(u_p, v_p)
    worst = cost
    used += 1
    if used == n - 1: break
 
sys.stdout.write(f"{worst}")