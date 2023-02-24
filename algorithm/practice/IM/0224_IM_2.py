# 숫자조작
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arrM = list(input())    # 최댓값
    arrM2 = arrM[:]         # 최솟값
    tmx = -1
    tidx = -1
    for i in range(len(arrM)-2):
        if arrM[i]== max(arrM[i:]):
            continue
        else:
            for j in range(i+1, len(arrM)):
                if int(arrM[j]) > tmx or int(arrM[j]) == tmx and j > tidx:
                    tmx = int(arrM[j])
                    tidx = j
            arrM[i], arrM[tidx] = str(tmx), arrM[i]
            break

    tmn = 999999999
    tidx = -1
    for i in range(len(arrM2)-2):
        if i == 0 and min(arrM2[i:]) == 0:          # 첫째자리이고 전체 최솟값이 0일 때
            for j in range(i, len(arrM2)):
                if int(arrM2[j]) != 0 and (int(arrM2[j]) < tmn or (int(arrM2[j]) == tmn and j > tidx)):
                    tmn = int(arrM2[j])
                    tidx = j
            arrM2[i], arrM2[tidx] = str(tmn), arrM2[i]
            break
        elif i == 0 and min(arrM2[i:]) != 0:        # 첫째자리이고 전체 최솟값이 0이 아닐 때
            tmp = arrM2.remove('0')
            print(tmp)
            if arrM2[i] == min(arrM2[i:]):          # 전체 최솟값이 첫째자리와 같음
                continue
            else:                                   # 전체 최솟값이 첫째자리와 다름
                for j in range(i, len(arrM2)):
                    if int(arrM2[j]) != 0 and (int(arrM2[j]) < tmn or (int(arrM2[j]) == tmn and j > tidx)):
                        tmn = int(arrM2[j])
                        tidx = j
                arrM2[i], arrM2[tidx] = str(tmn), arrM2[i]
                break
        else: # 첫째자리가 아님
            for j in range(i, len(arrM2)):
                    if int(arrM2[j]) < tmn or (int(arrM2[j]) == tmn and j > tidx):
                        tmn = int(arrM2[j])
                        tidx = j
            arrM2[i], arrM2[tidx] = str(tmn), arrM2[i]
            break

    print(f'#{tc} {arrM2} {arrM}')