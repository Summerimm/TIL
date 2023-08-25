# 뱀과 사다리 게임

# 최대한 사다리를 많이 타는 것이 이득
# 그리디하게 접근?
# 회의시간 문제랑 비슷한 듯
# 길이가 긴 사다리를 타는 게 이득?

import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
ladder, snake = map(int, input().split())

board = [0] * 101
for i in range(1, 101):
    board[i] = i


laddermx = 0
for _ in range(ladder):
    s, e = map(int, input().split())
    board[s] = e

for _ in range(snake):
    s, e = map(int, input().split())
    board[s] = e

print(board)



