from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

# 물고기가 가장 적은 어항에 물고기 한 마리 넣기
def push_fish_to_min_bowl(graph):
    min_bowl_fish_num = min(graph[0])
    for i in range(len(graph[0])):
        if graph[0][i] == min_bowl_fish_num:
            graph[0][i] += 1


# 가장 왼쪽의 어항을 위에 쌓기
def popleft_and_stack(graph):
    pop = graph[0].popleft()
    graph.append(deque([pop]))

# 공중에 뜬 어항들을 시계방향 90도 회전하기
def rotate_90_clockwise(bowls):
    new_bowls = [[0] * len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0])-1-i]

    return new_bowls

# 2개 이상 쌓인 어항들을 분리해서 공중부양 시키기
def fly_blocks(graph):
    while True:
        if len(graph) > len(graph[0]) - len(graph[-1]):
            break

        will_fly_blocks = []
        will_fly_blocks_row = len(graph)
        will_fly_blocks_col = len(graph[-1])

        for i in range(will_fly_blocks_row):
            new_deque = deque()
            for _ in range(will_fly_blocks_col):
                new_deque.append(graph[i].popleft())
            will_fly_blocks.append(new_deque)

        graph = [graph[0]]
        rotated_blocks = rotate_90_clockwise(will_fly_blocks)
        for row in rotated_blocks:
            graph.append(deque(row))

    return graph


N, K = map(int, sys.stdin.readline().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = list()
board.append(deque(list(map(int, sys.stdin.readline().split()))))

push_fish_to_min_bowl(board)
popleft_and_stack(board)
board = fly_blocks(board)


print(board)