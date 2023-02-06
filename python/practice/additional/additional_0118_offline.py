# 1. name와 age 라는 두개의 argument를 넘기면 각각 이 값을 출력하는 함수를 작성해보세요.
def func(name, age):
    print(f'{name}' +f'\n{age}')

name, age = map(str, input().split())
func(name, age)


# 2. 두 개의 매개변수가 있고, 이 매개변수들을 덧셈하고 뺄셈한 결과를 모두 반환하는 함수를 작성해 보세요.
def calculator(a, b):
    adder = a + b
    subtractor = a - b
    return adder, subtractor

calculator(5, 3)
print(calculator(5, 3))

# 3. 우리 회사 멤버의 이름과 연봉을 출력하는 함수를 만들어보세요.
# 매개변수는 이름과 연봉이 들어가는데, 만약 함수 호출에서 연봉이 누락되면 기본으로 4500이 나오도록 해주세요.
def company(name, income=4500):
    print(name, income)

company('김싸피', 8000)
company('이코딩')

# 4. n을 넘기면 1부터 n까지 더하는 my_sum 함수를 만들어보세요 (for 사용)
def my_sum(n):
    cnt = 0
    for i in range(n + 1):
        cnt += i
    return cnt

my_sum(10)
print(my_sum(10))

# 5. 4번을 while로 바꿔보세요
def my_sum(n):
    cnt = 0
    i = 0
    while(i <= n):
        cnt += i
        i += 1
    return cnt

my_sum(10)
print(my_sum(10))

# 6. 주어진 리스트에서 가장 큰 값을 찾아주는 함수를 작성해 보세요.
# ```
# num_list = [4, 6, 8, 24, 12, 2]
# ```
def maxfunc(numlist):
    numlist.sort()
    return numlist[-1]

num_list = [4, 6, 8, 24, 12, 2]
print(maxfunc(num_list))