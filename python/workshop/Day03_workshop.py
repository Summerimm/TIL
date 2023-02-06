# 1. 세로로 출력하기
# n = int(input())

# for i in range(1, n + 1):
#     print(i)
#-------------------------------
# 2. 가로로 출력하기
# n = int(input())

# for i in range(1, n + 1):
#     print(i, end = ' ')
#-------------------------------
# 3. 거꾸로 세로로 출력하기
# n = int(input())

# for i in range(n, -1, -1):
#     print(i)
#-------------------------------
# 4. 거꾸로 출력해 보아요
# n = int(input())

# for i in range(n, -1, -1):
#     print(i, end = ' ')
#-------------------------------
# 5. N줄 덧셈
# n = int(input())
# numsum = 0

# for i in range(n + 1):
#     numsum += i

# print(numsum)
#-------------------------------
# 6. 삼각형 출력하기
# n = int(input())

# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * i)
#-------------------------------
# 7. 중간값 찾기
numbers = [
    85, 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67, 
    51, 61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64,
    52, 90 , 60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24
]

numbers.sort()
print(numbers[len(numbers) // 2])