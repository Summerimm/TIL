# 뱀과 사다리 게임
import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
ladder, snake = map(int, input().split())

print(ladder, snake)
