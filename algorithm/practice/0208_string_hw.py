import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    t, l = map(str, input().split())
    l = int(l)
    st = list(map(str, input().split()))
    # 딕셔너리를 통해 문자열과 숫자를 매칭
    sdict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # 문자열을 숫자로 바꾸기
    for i, s in enumerate(st):
        st[i] = sdict[s] 
    # Bubble Sort
    for i in range(l-1, 0, -1):
        for j in range(i):
            if st[j] > st[j+1]:
                st[j], st[j+1] = st[j+1], st[j]
    # dictionary value에서 값을 찾아 key(문자열)로 변환
    for i, n in enumerate(st):
        for k, v in sdict.items():
            if v == n:
                st[i] = k
    # 출력
    print(f'#{tc}') 
    print(*st)