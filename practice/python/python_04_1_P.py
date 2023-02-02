# 맞는 비밀번호를 입력할 때까지 반복하는 코드를 작성하시오. 단, 비밀번호를 3회 이상 틀리면, 입력 기회가 종료된다.
ans = '0719'

for i in range(3):
    secret = input()
    if secret != ans:
        print("비밀번호가 올바르지 않습니다")
        continue
    else:
        print("열렸습니다")
        break

