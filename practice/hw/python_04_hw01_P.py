words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

try:
    for i in range(len(words)): # 0~6
        if words[i] in words[:i]:
            print(f'{i+1}번째 사람 탈락')
        else:
            if words[i][-1] != words[i+1][0]:
                print(f'{i+2}번째 사람 탈락')
            else:
                continue

except:
    pass