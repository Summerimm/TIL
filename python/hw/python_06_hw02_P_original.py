# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

edit = []
ana_lst = []
ans = []

def list_input():
    origin = list(map(str, input()[1:-1].split(',')))
    for c in origin:
        edit.append(c.strip("'"))
    return edit

list_input()
flag = [0] * len(edit)

for i in range(len(edit)-1):
    #print(edit[i])
    ana_lst = [edit[i]]
    #print(ana_lst)
    for j in range(i+1, len(edit)):
        #print(edit[j])
        if len(edit[i]) == len(edit[j]): # 비교하는 두 문자열의 길이가 같을 때
            #print("비교하는 두 문자열의 길이가 같을 때")
            flag_num = 0 # flag = 0으로 두고 애너그램 비교 시작
            if flag[j] == 1: # 이미 set 만들어져 있음
                #print("이미 set 만들어져 있음")
                continue
            else: 
                for c in edit[i]: # 하나를 기준으로 문자열 순회
                    #print("하나를 기준으로 문자열 순회")
                    if edit[i].count(c) == edit[j].count(c):  # 각 단어 내의 문자 수가 같을 때
                        #print("각 단어 내의 문자 수가 같을 때")
                        flag_num = 1 # flag = 0
                        continue
                    else:
                        #print("각 단어 내의 문자 수가 다를 때")
                        flag_num = 0 # flag = 0
                        break # 반복 종료
                if flag_num == 1: # 끝까지 1 유지(애너그램)
                    #print("끝까지 1 유지(애너그램)")
                    #print(edit[i], edit[j])
                    flag[i] = 1
                    flag[j] = 1
                    ana_lst.append(edit[j]) # 애너그램 lst에 추가
                    #print(ana_lst)
        else: # 비교하는 문자열 길이 다를 때
            #print("비교하는 문자열 길이 다를 때")
            continue
    if ana_lst == [edit[i]]:
        continue
    else:
        ans.append(ana_lst) # 애너그램 비교 끝
        #print(ans)

for idx, num in enumerate(flag):
    if num == 0:
        lst = []
        lst.append(edit[idx])
        ans.append(lst)

print(ans)