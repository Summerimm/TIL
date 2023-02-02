# 문제
# n개의 소금물을 섞었을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램 mass_percent.py를 만드시오. 

# 조건    
# - 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.        
# 최대 5개의 소금물을 입력할 수 있다. 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

cnt = 0
saltlist = []
while(cnt < 5):
        cnt += 1
        input_string = input(f'{cnt}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
        if input_string == 'Done':
            break
        else:
            input_string = input_string.replace('%', '')
            input_string = input_string.replace('g', '')
            saltlist.append(list(map(int, input_string.split())))

total, salt = 0.0, 0
for percent, amount in saltlist:
    total += amount
    salt += amount * (0.01 * percent)

salt_percent = round(salt/total * 100, 2)
total = round(total, 2)

print(f'{salt_percent}% {total}g')