# 알파벳 순서로 정렬 후, 각 알파벳의 개수가 같으면 애너그램

# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']
# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(words):
    word_dic = {} # {ate: {~}, tea: {~}...}
    for word in words:
        sub_dic = {} # {a: 1, e: 1, t: 1}
        for char in word: #  a, e, t...
            if char in sub_dic: # 이미 존재하는 알파벳
                sub_dic[char] += 1
            else: # 새로운 알파벳
                sub_dic[char] = 1
        word_dic[word] = sub_dic # ate key에 {a: 1, e: 1, t: 1} value 매칭

    anagram = []
    for word in words: # 'tea' - 'ate'
        for ana_list in anagram: # 'eat' - 'eat', 'tea'
            ana_word = ana_list[0] # 'eat' - 'eat'
            if word_dic[word] == word_dic[ana_word]: # tea와 eat의 알파벳 개수 비교해서 같은 상황
                ana_list.append(word) # ana_list에 tea를 추가, ate를 추가
                break
        else:
            anagram.append([word]) # 'eat'이 존재하지 않으므로 추가
    return anagram        

print(group_anagrams(words))


words = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(words):
    anagrams = {}

    for word in words: # 'eat'
        sorted_word = sorted(word) # ['a', 'e', 't']
        key = ''.join(sorted_word) # 'aet'

        if key in anagrams: # anagram 그룹에 해당
            anagrams[key].append(word)
        else: # dictionary 안에 해당 단어가 존재하지 않는 경우
            anagrams[key] = [word]

    return list(anagrams.values())
print(group_anagrams(words))