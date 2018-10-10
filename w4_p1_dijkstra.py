#Uses python3

import sys
import queue
import heapq as h
import itertools

class priorityQueueWrap:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-node>'
        self.counter = itertools.count()

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        h.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = h.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return (len(self.entry_finder) == 0)

def distance(adj, cost, s, t):
    #write your code here
    dist = [len(adj)*1000] * len(adj)
    prev = [None] * len(adj)
    dist[s]=0
    H = priorityQueueWrap()
    for v in range(len(dist)): H.add_task(v,dist[v])
#    print(H.empty())
    while not H.empty():
#        print(H.pq)
#        print(H.entry_finder)
#        print(dist)
        u = H.pop_task()
#        (d, c, u )= H.pop_task()
        for v in range(len(adj[u])):
#            print('{}: {},{}: {}'.format(adj[u][v], dist[adj[u][v]],u,cost[u][v]))
            if dist[adj[u][v]] > (dist[u] + cost[u][v]):
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u
                H.add_task(adj[u][v],dist[adj[u][v]])
    if dist[t] == len(adj)*1000: return -1
    return dist[t]
#    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
