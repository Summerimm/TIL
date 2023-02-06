# 문제
# 같은 숫자가 한 개 있거나 두 개가 들어있는 리스트가 주어진다.
# 이러한 리스트에서 숫자가 한 개만 있는 요소들의 합을 구하는 함수 sum_of_repeat_number()를 작성하시오.
# 예를 들어, [4, 4, 7, 8, 10, 4]는 7과 8, 10이 한번만 나오기 때문에 세 개를 더한 25가 결과값으로 도출된다. 

# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(data):
    numdict = {}
    sum = 0

    for num in data:
        if num in numdict.keys():
            numdict[num] += 1
        else:
            numdict[num] = 1

    for keynum, cnt in numdict.items():
        if cnt == 1:
            sum += keynum

    return sum

num_list = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_number(num_list))
