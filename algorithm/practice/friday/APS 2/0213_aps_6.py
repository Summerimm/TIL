# 다솔이의 다이아몬드 장식
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s = list(input())
    l = len(s)
    if l == 1:
        print('..#..')
        print('.#.#.')
        print(f'#.{s[0]}.#')
        print('.#.#.')
        print('..#..')
    else:
        print('..#.' * l+'.')
        print('.#.#' * l + '.')
        for i in range(l):
            print(f'#.{s[i]}.', end='')
        print('#')
        print('.#.#' * l + '.')
        print('..#.' * l + '.')