import collections
import numpy as np

q = collections.deque()

f = False

#   A B C D E F
# A  0 3 2 0 0 5
# B  3 0 1 6 0 0
# C  2 1 0 3 4 0
# D  0 6 3 0 3 0
# E  0 0 4 3 0 2
# F  0 6 3 0 2 0

dist = [
    [0, 3, 2, 0, 0, 5],
    [3, 0, 1, 6, 0, 0],
    [2, 1, 0, 3, 4, 0],
    [0, 6, 3, 0, 3, 0],
    [0, 0, 4, 3, 0, 2],
    [5, 0, 0, 0, 2, 0]
]

par = [-1 for i in range(len(dist))]
cityDict = {
    0: "Mumbai",
    1: "bengluru",
    2: "hyderabad",
    3: "kolkata",
    4: "Lucknow",
    5: "New delhi"
}

v = np.zeros(len(dist))


def addNeighbours(node):
    global f
    for idx, i in enumerate(dist[node]):
        if i != 0 and v[idx] != 1:

            v[idx] = 1
            par[idx] = node
            q.append(idx)


def BFS(start, end):
    global f
    q.append(start)
    v[start] = 1
    while len(q) != 0 and f == False:
        node = q.popleft()
        addNeighbours(node)


def iterate(start, end):
    k = end
    ans = []
    while k != -1:
        ans.append(k)
        k = par[k]

    total = 0
    prev = end

    for i in reversed(ans):
        print(cityDict[i]+"->", end=" ")
        total = total + dist[prev][i]
        prev = i

    print("\ntotal cost: " + str(total))


for key in cityDict:
    print(str(key)+": "+cityDict[key])
print()
start = int(input("Enter start node: "))
end = int(input("Enter end node: "))
print()
BFS(start, end)
iterate(start, end)
