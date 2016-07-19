# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 7. 16.
'''


import sys
import math
from heapq import *
from collections import defaultdict

rl = lambda : sys.stdin.readline()


def sovle(buildings, LAN):
    # shortest distance algorithms
    # prim

    # mst = []
    visited = set([0])
    result_distance = 0

    edge = LAN[0]
    # print edge

    heapify(edge)
    # print heapq.heappop(edge)

    while edge:
        cost, node_from, node_to = heappop(edge)
        # print heappop(edge)
        if node_to not in visited:
            visited.add(node_to)
            # mst.append((cost,node_from,node_to))
            result_distance += cost

            for node in LAN[node_to]:
                if node[2] not in visited:
                    heappush(edge, node)

    # for node in mst:
    #     result_distance += node[0]
        # print node[0]


    # print result_distance
    # return mst
    return result_distance


def point_sqrt(x, y):
    return math.sqrt( (x[0]-y[0])**2 + (x[1] - y[1])**2)

'''
def set_LAN2(buildings, linked, points):
#     LAN distance setting
    LAN = [ [ float('inf') for x in xrange(buildings) ] for x in xrange(
        buildings) ]

    A_LAN = defaultdict(list)

    for index in xrange(buildings):
        for inner_index in xrange(buildings):
            if index is inner_index:
                continue
            elif index in linked.keys():
                if inner_index in linked[index]:
                    LAN[index][inner_index] = 0.0
                    LAN[inner_index][index] = 0.0
                else:
                    LAN[index][inner_index] = point_sqrt(points[index],
                                                         points[inner_index])
                    A_LAN[index].append((point_sqrt(points[index],points[inner_index]),
                                         index,
                                         inner_index))
            else:
                LAN[index][inner_index] = point_sqrt(points[index],
                                                     points[inner_index])

'''




def set_LAN(buildings, linked, points):
    # LAN distance setting
    LAN = defaultdict(list)

    for index in xrange(buildings):
        for inner_index in xrange(buildings):
            if index is inner_index:
                continue
            elif index in linked.keys():
                if inner_index in linked[index]:
                    LAN[index].append((0.0, index, inner_index))
                else:
                    LAN[index].append((point_sqrt(points[index],points[inner_index]),
                                         index,
                                         inner_index))
            else:
                LAN[index].append((point_sqrt(points[index],points[inner_index]),
                                     index,
                                     inner_index))
    # print LAN
    # print linked

    # sovle(buildings, LAN)
    # print LAN
    return LAN


def set_linked(cables):
    ## link setting
    linked = dict()
    for cable in xrange(cables):
        linked_from, linked_to =  map(int, rl().rstrip().split())
        try:
            # linked[linked_from].append(linked_to)
            linked[linked_from].add(linked_to)
            # linked[linked_to].add(linked_from)
        except KeyError:
            # linked[linked_from] = [linked_to]
            linked[linked_from] = set()
            linked[linked_from].add(linked_to)
            # linked[linked_to] = set()
            # linked[linked_to].add(linked_from)
        try:
            linked[linked_to].add(linked_from)
        except KeyError:
            linked[linked_to] = set()
            linked[linked_to].add(linked_from)
    return linked




def main():
    for tc in xrange(int(rl())):
        # input setting
        buildings, cables = map(int, rl().rstrip().split())
        points_of_x = map(int, rl().rstrip().split())
        points_of_y = map(int, rl().rstrip().split())
        points = zip(points_of_x, points_of_y)
        # print points

        # print linked
        linked = set_linked(cables)

        #set LAN
        LAN = set_LAN(buildings, linked, points)

        # print sovle(buildings, LAN)
        print sovle(buildings, LAN)

if __name__ == "__main__":
    main()