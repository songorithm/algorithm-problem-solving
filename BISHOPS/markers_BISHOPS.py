# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 7. 31.
'''


import sys

rl = lambda : sys.stdin.readline()


direction = [(-1,1), (1,1)]

def input():
    global board_size
    board_size = int(rl())
    global board
    board = [ None ] * board_size
    for index in xrange(board_size):
        board[index] = list(rl().rstrip())



def define_line_number(edge, count):
    for dir in xrange(2):
        for y in xrange(board_size):
            for x in xrange(board_size):
                if board[y][x] == "." and edge[dir][y][x] == None:
                    current_x, current_y = x, y
                    while 0 <= current_x < board_size and 0 <= current_y < board_size \
                            and board[current_y][current_x] == ".":
                        edge[dir][current_y][current_x] = count[dir]
                        current_x += direction[dir][0]
                        current_y += direction[dir][1]

                    count[dir] += 1
    return edge, count



def make_adj_matrix(edge):
    adj_matrix = [ [None] * 64 for x in xrange(64) ]
    for y in xrange(board_size):
        for x in range(board_size):
            if board[y][x] == ".":
                adj_matrix[ edge[0][y][x] ][ edge[1][y][x] ] = 1
    return adj_matrix


def dfs(u_index, adj_matrix):
    if visited[u_index]:
        return False

    visited[u_index] = True

    for v_index in xrange(v):
        if adj_matrix[u_index][v_index]:
            if v_lines[v_index] == None or dfs(v_lines[v_index], adj_matrix):
                u_lines[u_index] = v_index
                v_lines[v_index] = u_index
                return True

    return False


def bipartite_match(adj_matrix):
    global u_lines, v_lines
    u_lines = [ None ] * u
    v_lines = [ None ] * v
    size = 0
    global visited

    for u_index in xrange(u):
        visited = [ False ] * u
        if dfs(u_index, adj_matrix):
            size += 1

    return size


def main():
    for tc in xrange(int(rl())):

        # initalize
        # array[2][8][8]
        edge = [ [ [ None ] * 8 for x in xrange(8) ] for x in xrange(2) ]
        count = [0,0]

        input()

        edge, count = define_line_number(edge,count)

        global u, v
        u,v = count

        adj_matrix = make_adj_matrix(edge)

        print bipartite_match(adj_matrix)



if __name__ == "__main__":
    main()