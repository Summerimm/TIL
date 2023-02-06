# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    num_list = list(map(int, str(n)))
    return sum(num_list) + n

def is_selfnumber(n):
    notselfnum = set()
    for i in range(1, n):
        notselfnum.add(fn_d(i))
    if n in notselfnum:
        return False
    else:
        return True

n = int(input())
print(fn_d(n))
print(is_selfnumber(n))