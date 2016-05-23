import numpy
from heapq import *


def getHeuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(elementList, start, endNode):

    adjacent = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    prev = {}
    g = {start:0}
    fscore = {start:getHeuristic(start, endNode)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:
        current = heappop(oheap)[1]
        if current == endNode:
            list1 = []
            while current in prev:
                list1.append(current)
                current = prev[current]
            return list1

        close_set.add(current)
        for i, j in adjacent:
            neighbNode = current[0] + i, current[1] + j
            tentative_g_score = g[current] + getHeuristic(current, neighbNode)
            if 0 <= neighbNode[0] < elementList.shape[0]:
                if 0 <= neighbNode[1] < elementList.shape[1]:
                    if elementList[neighbNode[0]][neighbNode[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            if neighbNode in close_set and tentative_g_score >= g.get(neighbNode, 0):
                continue

            if  tentative_g_score < g.get(neighbNode, 0) or neighbNode not in [i[1]for i in oheap]:
                prev[neighbNode] = current
                g[neighbNode] = tentative_g_score
                fscore[neighbNode] = tentative_g_score + getHeuristic(neighbNode, endNode)
                heappush(oheap, (fscore[neighbNode], neighbNode))

    return False

nmap = numpy.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1],
    [1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1],
    [1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])




print astar(nmap, (1,1), (17,17))
