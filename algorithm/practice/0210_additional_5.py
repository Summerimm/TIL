# 회문2
import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):###########11
    t = int(input())
    p1 = [list(input()) for _ in range(100)] ############100
    p2 = list(zip(*p1))
    mx = 0
    for i in range(100):
        for j in range(100):
            for k in range(1, 101-j):
                str1 = p1[i][j:j+k]
                str2 = p2[i][j:j+k]
                if str1 == str1[::-1] and (len(str1) > mx):
                    mx = len(str1)
                if str2 == str2[::-1] and (len(str2) > mx):
                    mx = len(str2)
    print(f'#{t}', mx)


# 1
# CBCABBAC
# BBABCABA
# ABCBCACA
# BACCAABB
# BCBCACBC
# CABACCCB
# CAAACCAB
# CBABACAC