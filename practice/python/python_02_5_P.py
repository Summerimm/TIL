# 문제
# 다음과 같이 tuple를 저장한 list가 있다. 
# 각 tuple의 첫 번째 요소는 해야할 일, 두 번째 요소는 남은 일 수이다.
# 새로운 일정을 입력받아 list에 추가하고 출력하라.

# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

# 해야 할 일, 그리고 남은 일수까지 총 두 번 입력받는다.
# 입력받은 해야 할 일과 남은 일수는 tuple로 묶는다.
# 남은 일수는 int 형태로 저장한다.

# 입력예시
# Soccer Contest
# 10
# 출력예시
# [("Python Homework", 3), ("Assay", 4), ("Vacation", 100), ("Soccer Contest", 10)]


todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

work = input()
days = int(input())
addtodo = (work, days)

todo.append(addtodo)
print(todo)