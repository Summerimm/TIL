words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

word_dic = {}
for word in words:
    sub_dic = {}
    for char in word:
        if char in sub_dic.keys():
            sub_dic[char] += 1
        else:
            sub_dic[char] = 1
    word_dic[word] = sub_dic

anagram = []
for word, sub_dic in word_dic.items():
    for analist in anagram: # anagram = [['eat', 'ate', 'tea'], ['tan'...]]
        anaword = analist[0]
        if word_dic[anaword] == word_dic[word]:
            analist.append(word)
            break
    else:
        anagram.append([word])

print(anagram)