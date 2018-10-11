#Uses python3

import sys
import math

def bf(adj,cost,s=0):
    dist = [len(adj)*1000] * len(adj)
    prev = [None] * len(adj)
    cycle = []
    dist[s]=0
    for i in range(len(adj)-1):
        for u in range(len(adj)):
            for v in range(len(cost[u])):
                if dist[adj[u][v]] > (dist[u] + cost[u][v]):
                    dist[adj[u][v]] = dist[u] + cost[u][v]
                    prev[adj[u][v]] = u
#    print(dist)
    for u in range(len(cost)):
        for v in range(len(cost[u])):
            if dist[adj[u][v]] > (dist[u] + cost[u][v]):
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u
                return 1
    return 0

def negative_cycle(adj, cost):
    #write your code here
    #bf(adj,cost)

    return bf(adj,cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
