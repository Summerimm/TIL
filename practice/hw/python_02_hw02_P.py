orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

order_list = list(map(str, orders.split(',')))
order_set = set(order_list)
ice = 0

for c2 in order_list:
        if '아이스' in c2:
            ice += 1
print('아이스 음료 주문 수: '+ f'{ice}')

for c1 in order_set:
    cnt = 0
    for c2 in order_list:
        if c2 == c1:
            cnt += 1
    print(f'{c1}: ' + f'{cnt}')
