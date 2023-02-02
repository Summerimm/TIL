# 1. 간단한 N의 약수
# n = int(input())
# lst = []

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end = ' ')
#-------------------------------
# 2. List의 합 구하기
# def list_sum(data):
#     total = 0
#     for i in num:
#         total += i
#     return total

# num = [1, 2, 3, 4, 5]
# print(list_sum(num))
#-------------------------------
# 3. Dictionary로 이루어진 List의 합 구하기
def dict_list_sum(data):
    age_sum = 0
    for i in data:
        age_sum += i['age']
    return age_sum

namedata = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
print(dict_list_sum(namedata))
#-------------------------------
# 4. 2차원 List의 전체 합 구하기
# def all_list_num(data):
#     list_sum = 0
#     for i in range(len(num_list)):
#         for j in range(len(num_list[i])):
#             list_sum += num_list[i][j]
#     return list_sum

# num_list = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
# print(all_list_num(num_list))
#-------------------------------
# 5. 숫자의 의미
# def get_secret_word(data):
#     char = ''
#     for i in data:
#         char += chr(i)
#     return char

# secret = [83, 115, 65, 102, 89]
# print(get_secret_word(secret))
#-------------------------------
# 6. 내 이름은 몇일까?
# def get_secret_number(string):
#     ascii_sum = 0
#     for i in range(len(string)):
#         ascii_sum += ord(string[i])
#     return ascii_sum

# print(get_secret_number('happy'))
#-------------------------------
# 7. 내 이름은 몇일까?
# def get_strong_word(str1, str2):
#     ascii_sum1, ascii_sum2 = 0, 0
#     for i in range(len(str1)):
#         ascii_sum1 += ord(str1[i])
#     for i in range(len(str2)):
#         ascii_sum2 += ord(str2[i])
#     if ascii_sum1 > ascii_sum2:
#         return str1
#     elif ascii_sum1 < ascii_sum2:
#         return str2
#     else:
#         return str1, str2

# print(get_strong_word('z', 'a'))
# print(get_strong_word('delilah', 'dixon'))
# print(get_strong_word('dixon', 'dixon'))