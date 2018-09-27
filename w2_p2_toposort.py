#Uses python3

import sys

def explore(adj,u,o,x):
  u[x]=1
  for y in adj[x]:
    if u[y]==0:
        explore(adj,u,o,y)
  o.append(x)
  return 0

def dfs(adj, used, order):
    #write your code here
    for x in range(len(adj)):
        if used[x]==0: explore(adj,used,order,x)
    return

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    dfs(adj, used, order)
#    for x in range(len(adj)):
#        if used[x]==0: dfs(adj,used,order,x)
    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

