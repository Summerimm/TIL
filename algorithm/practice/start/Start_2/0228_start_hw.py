# 암호 코드 스캔
import sys
sys.stdin = open('input.txt', 'r')

dct = {'211':0,'221':1,'122':2,'411':3,'132':4,'231':5,'114':6,'312':7,'213':8,'112':9}

def solve():
    ans = set()
    for st in sset:
        # 16진수 문자열 => 2진수 문자열로
        bst = bin(int(st, 16)).replace('0b', '').zfill(4*len(st))
        print(bst)
        # 연속한 0/1의 개수 저장
        cnts = []
        old = 0
        for i in range(len(bst)):
            if bst[old] != bst[i]:
                cnts.append(i-old)
                old = i

        # 단위두께로 나누어서 암호로 변환
        pwd = []
        for i in range(1, len(cnts), 4):
            mn = min(cnts[i:i+3])
            key = str(cnts[i]//mn)+str(cnts[i+1]//mn)+str(cnts[i+2]//mn)
            pwd.append(dct[key])
        
        # pwd의 8자리씩 코드를 중복제거
        for i in range(0, len(pwd), 8):
            ans.add(tuple(pwd[i:i+8]))
    
    # ans에서 암호코드를 하나씩 꺼내서 검증 후 정상이면 누적
    sm = 0
    for lst in ans:
        if (sum(lst[0:8:2])*3 + sum(lst[1:8:2]))%10 == 0:   # 정상인 경우 누적
            sm += sum(lst)
    return sm

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력 문자열 중복제거
    sset = set()
    for _ in range(N):
        st = input()
        if st.count('0') != len(st):
            sset.add(st)
    print(f'#{tc} {solve()}')