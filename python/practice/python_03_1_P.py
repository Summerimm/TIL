# 목표
#리스트를 for문을 통해 변환하며, 이에 대한 응용력을 키운다.

# 문제
# 과수원에 농부 한 명이 썩은 과일이 몇 개 들어있는 과일 봉지를 가지고 있다. 
# 과일 봉지를 입력받아, 썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 리스트 형식으로 출력하시오.
# 	예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우, 대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.

# 유의 사항
# n 만약 리스트가 비어 있는 경우 빈 리스트를 반환한다.
# n 반환된 리스트의 요소는 모두 소문자여야 한다.

fruits = list(map(str, input().split(',')))
lowerfruits = []
ans = []

if fruits == ['']:
    print('[]')

else:
    for i, f in enumerate(fruits):
        lowerfruits.append(f.lower())

    for i, f in enumerate(lowerfruits):
        if 'rotten' in f:
            ans.append(f[6:])
        else:
            ans.append(f)
            
    print(ans)