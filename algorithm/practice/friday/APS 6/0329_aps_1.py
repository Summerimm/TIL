# 정식이의 은행업무
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    b, t = input(), input()
    b_len, t_len = len(b), len(t)
    b_list, t_list = [], []

    for i in range(b_len):
        if b[i] == '0':
            tmp = b[:i] + '1' + b[i+1:]
            b_list.append(int(tmp, 2))
        else:
            tmp = b[:i] + '0' + b[i+1:]
            b_list.append(int(tmp, 2))

    for i in range(t_len):
        if t[i] == '0':
            tmp1 = t[:i] + '1' + t[i+1:]
            tmp2 = t[:i] + '2' + t[i+1:]
            t_list.append(int(tmp1, 3))
            t_list.append(int(tmp2, 3))
        elif t[i] == '1':
            tmp1 = t[:i] + '0' + t[i+1:]
            tmp2 = t[:i] + '2' + t[i+1:]
            t_list.append(int(tmp1, 3))
            t_list.append(int(tmp2, 3))
        else:
            tmp1 = t[:i] + '0' + t[i+1:]
            tmp2 = t[:i] + '1' + t[i+1:]
            t_list.append(int(tmp1, 3))
            t_list.append(int(tmp2, 3))
    
    for bi in b_list:
        if bi in t_list:
            print(f'#{tc}', bi)
            break